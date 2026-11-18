param(
    [string]$Source = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$Target = (Join-Path $env:USERPROFILE '.codex\skills\industry-bottleneck-audit')
)

$ErrorActionPreference = 'Stop'
$sourcePath = (Resolve-Path -LiteralPath $Source).Path.TrimEnd('\')
$targetPath = [System.IO.Path]::GetFullPath($Target).TrimEnd('\')
if ($sourcePath -eq $targetPath) {
    throw 'Source and target must be different directories.'
}

if (Test-Path -LiteralPath $targetPath -PathType Container) {
    $targetItem = Get-Item -LiteralPath $targetPath -Force
    if (($targetItem.Attributes -band [System.IO.FileAttributes]::ReparsePoint) -ne 0) {
        $linkTarget = @($targetItem.Target)[0]
        if ($linkTarget) {
            if (-not [System.IO.Path]::IsPathRooted($linkTarget)) {
                $linkTarget = Join-Path $targetItem.Parent.FullName $linkTarget
            }
            $resolvedLinkTarget = [System.IO.Path]::GetFullPath($linkTarget).TrimEnd('\')
            if ($resolvedLinkTarget -eq $sourcePath) {
                Write-Output "Skill target is already linked to the verified source at $sourcePath"
                return
            }
        }
    }
}

New-Item -ItemType Directory -Force -Path $targetPath | Out-Null
$prefix = $sourcePath + '\'
$sourceFiles = Get-ChildItem -LiteralPath $sourcePath -File -Recurse -Force |
    Where-Object { $_.FullName -notlike '*\__pycache__\*' -and $_.Extension -ne '.pyc' }
foreach ($file in $sourceFiles) {
    $relative = $file.FullName.Substring($prefix.Length)
    $installed = Join-Path $targetPath $relative
    New-Item -ItemType Directory -Force -Path (Split-Path $installed) | Out-Null
    Copy-Item -LiteralPath $file.FullName -Destination $installed -Force
}

$mismatches = foreach ($file in $sourceFiles) {
    if ($file.FullName -like '*\__pycache__\*' -or $file.Extension -eq '.pyc') {
        continue
    }
    $relative = $file.FullName.Substring($prefix.Length)
    $installed = Join-Path $targetPath $relative
    if (-not (Test-Path -LiteralPath $installed -PathType Leaf)) {
        "missing: $relative"
        continue
    }
    if ((Get-FileHash -LiteralPath $file.FullName -Algorithm SHA256).Hash -ne
        (Get-FileHash -LiteralPath $installed -Algorithm SHA256).Hash) {
        "hash mismatch: $relative"
    }
}

if ($mismatches) {
    throw "Skill installation verification failed:`n$($mismatches -join "`n")"
}

Write-Output "Installed and verified industry-bottleneck-audit at $targetPath"
