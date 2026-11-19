param(
    [string]$Root = (Resolve-Path (Join-Path $PSScriptRoot '..')).Path,
    [string]$PrivateDenylist = $env:INDUSTRY_BOTTLENECK_PRIVATE_DENYLIST
)

$ErrorActionPreference = 'Stop'
$env:PYTHONDONTWRITEBYTECODE = '1'
$rootPath = (Resolve-Path -LiteralPath $Root).Path
$errors = [System.Collections.Generic.List[string]]::new()

$files = Get-ChildItem -LiteralPath $rootPath -Recurse -Force -File |
    Where-Object { $_.FullName -notlike '*\.git\*' }

$allowlistPath = Join-Path $rootPath 'scripts\public-files.allowlist'
if (-not (Test-Path -LiteralPath $allowlistPath -PathType Leaf)) {
    $errors.Add('missing exact public file allowlist: scripts/public-files.allowlist')
} else {
    $allowed = Get-Content -LiteralPath $allowlistPath |
        ForEach-Object { $_.Trim().Replace('\', '/') } |
        Where-Object { $_ -and -not $_.StartsWith('#') } |
        Sort-Object -Unique
    $actual = $files |
        ForEach-Object { $_.FullName.Substring($rootPath.Length + 1).Replace('\', '/') } |
        Sort-Object -Unique

    foreach ($path in $actual | Where-Object { $_ -notin $allowed }) {
        $errors.Add("file is not in public allowlist: $path")
    }
    foreach ($path in $allowed | Where-Object { $_ -notin $actual }) {
        $errors.Add("allowlisted file is missing: $path")
    }
}

foreach ($file in $files) {
    if ($file.Name -eq '.env' -or $file.Name -like '.env.*' -or
        $file.Extension -in @('.pem', '.key', '.pyc', '.pyo') -or
        $file.FullName -like '*\__pycache__\*' -or
        $file.FullName -like '*\.playwright-mcp\*') {
        $errors.Add("forbidden file: $($file.FullName.Substring($rootPath.Length + 1))")
    }

    if ($file.Name -match '(?i)(blind-map|answer-key|private|sealed|holdout|contaminated)') {
        $errors.Add("private or evaluation artifact name: $($file.FullName.Substring($rootPath.Length + 1))")
    }
}

$textExtensions = @('.md', '.txt', '.json', '.yaml', '.yml', '.csv', '.py', '.ps1', '.sh', '.html', '.js', '.mjs')
$secretPattern = '(sk-[A-Za-z0-9]{20,}|ghp_[A-Za-z0-9]{20,}|github_pat_[A-Za-z0-9_]{20,}|AKIA[0-9A-Z]{16}|-----BEGIN (RSA |EC |OPENSSH )?PRIVATE KEY-----|AIza[0-9A-Za-z_-]{30,})'
# Reject generic drive-rooted and home paths; keep machine-specific terms in the private denylist.
$localPathPattern = '(?i)((?<![A-Z0-9_])[A-Z]:[\\/]|/Users/[^/]+/|/home/[^/]+/)'

foreach ($file in $files | Where-Object {
    $_.Extension -in $textExtensions -and $_.FullName -ne $PSCommandPath
}) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    if ($content -match $secretPattern) {
        $errors.Add("credential-like content: $($file.FullName.Substring($rootPath.Length + 1))")
    }
    if ($content -match $localPathPattern) {
        $errors.Add("absolute local path: $($file.FullName.Substring($rootPath.Length + 1))")
    }
}

if ($PrivateDenylist) {
    if (-not (Test-Path -LiteralPath $PrivateDenylist -PathType Leaf)) {
        $errors.Add('configured private denylist does not exist')
    } else {
        $privateTerms = Get-Content -LiteralPath $PrivateDenylist |
            ForEach-Object { $_.Trim() } |
            Where-Object { $_ -and -not $_.StartsWith('#') }
        foreach ($file in $files | Where-Object {
            $_.Extension -in $textExtensions -and $_.FullName -ne $PSCommandPath
        }) {
            $content = Get-Content -LiteralPath $file.FullName -Raw
            foreach ($term in $privateTerms) {
                if ($content.IndexOf($term, [System.StringComparison]::OrdinalIgnoreCase) -ge 0) {
                    $errors.Add("private denylist match: $($file.FullName.Substring($rootPath.Length + 1))")
                    break
                }
            }
        }
    }
}

$gitDir = Join-Path $rootPath '.git'
if (Test-Path -LiteralPath $gitDir) {
    $historicalPaths = & git -C $rootPath log --all --name-only --pretty=format: 2>$null
    foreach ($path in $historicalPaths | Where-Object { $_ }) {
        if ($path -match '(?i)(blind-map|answer-key|private|sealed|holdout|contaminated)') {
            $errors.Add("private or evaluation artifact name in Git history: $path")
        }
    }

    if ($PrivateDenylist -and (Test-Path -LiteralPath $PrivateDenylist -PathType Leaf)) {
        foreach ($term in $privateTerms) {
            $historyHit = & git -C $rootPath log --all --format=%H -S $term -- 2>$null | Select-Object -First 1
            if ($historyHit) {
                $errors.Add('private denylist content exists in Git history')
                break
            }
        }
    }
}

foreach ($file in $files | Where-Object { $_.Extension -eq '.md' }) {
    $content = Get-Content -LiteralPath $file.FullName -Raw
    $links = [regex]::Matches($content, '\[[^\]]*\]\(([^)]+)\)')
    foreach ($link in $links) {
        $target = $link.Groups[1].Value.Trim().Trim('<', '>')
        if ($target -match '^(?i)(https?://|mailto:|#)' -or $target -match '^\$') {
            continue
        }
        $pathPart = ($target -split '#', 2)[0]
        if ([string]::IsNullOrWhiteSpace($pathPart)) {
            continue
        }
        $resolved = Join-Path $file.DirectoryName $pathPart
        if (-not (Test-Path -LiteralPath $resolved)) {
            $relativeFile = $file.FullName.Substring($rootPath.Length + 1)
            $errors.Add("broken relative link in ${relativeFile}: $target")
        }
    }
}

if ($errors.Count -gt 0) {
    $errors | Sort-Object -Unique | ForEach-Object { Write-Error $_ }
    throw "Prepublish content scan failed with $($errors.Count) finding(s)."
}

$skill = Join-Path $rootPath 'skill\industry-bottleneck-audit'
$validator = Join-Path $skill 'scripts\validate_audit_bundle.py'
$bundle = Join-Path $skill 'examples\minimal-audit-bundle.json'

& python -X utf8 $validator --self-test
if ($LASTEXITCODE -ne 0) { throw 'Audit-bundle self-test failed.' }

& python -X utf8 $validator $bundle
if ($LASTEXITCODE -ne 0) { throw 'Minimal audit bundle validation failed.' }

& python -X utf8 -m unittest (Join-Path $skill 'scripts\test_validate_audit_bundle.py')
if ($LASTEXITCODE -ne 0) { throw 'Audit-bundle unit tests failed.' }

& python -X utf8 -m unittest (Join-Path $skill 'scripts\test_render_audit_visual.py')
if ($LASTEXITCODE -ne 0) { throw 'Visual renderer unit tests failed.' }

& powershell -NoProfile -ExecutionPolicy Bypass -File (Join-Path $skill 'scripts\test_install_skill.ps1')
if ($LASTEXITCODE -ne 0) { throw 'Installation smoke test failed.' }

$quickValidate = Join-Path $env:USERPROFILE '.codex\skills\.system\skill-creator\scripts\quick_validate.py'
if (Test-Path -LiteralPath $quickValidate -PathType Leaf) {
    & python -X utf8 $quickValidate $skill
    if ($LASTEXITCODE -ne 0) { throw 'Skill structure validation failed.' }
} else {
    Write-Warning 'Codex quick_validate.py was not found; run it in a Codex development environment before tagging.'
}

Write-Output "PASS: public package scan and tests completed for $rootPath"

