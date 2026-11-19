$source = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path
$tempRoot = Join-Path ([System.IO.Path]::GetTempPath()) ("industry-bottleneck-install-" + [guid]::NewGuid())
$target = Join-Path $tempRoot 'industry-bottleneck-audit'

try {
    & (Join-Path $PSScriptRoot 'install_skill.ps1') -Source $source -Target $target | Out-Null
    & (Join-Path $PSScriptRoot 'install_skill.ps1') -Source $source -Target $target | Out-Null

    if (-not (Test-Path -LiteralPath (Join-Path $target 'SKILL.md') -PathType Leaf)) {
        throw 'Installed SKILL.md is missing.'
    }
    if (Test-Path -LiteralPath (Join-Path $target 'industry-bottleneck-audit') -PathType Container) {
        throw 'Repeated installation created a nested skill directory.'
    }
    Write-Output 'Install test passed: first install and repeated upgrade are idempotent.'
}
finally {
    if (Test-Path -LiteralPath $tempRoot) {
        $resolvedTemp = [System.IO.Path]::GetFullPath($tempRoot)
        $systemTemp = [System.IO.Path]::GetFullPath([System.IO.Path]::GetTempPath())
        if ($resolvedTemp.StartsWith($systemTemp, [System.StringComparison]::OrdinalIgnoreCase)) {
            Remove-Item -LiteralPath $resolvedTemp -Recurse -Force
        }
    }
}
