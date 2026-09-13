[CmdletBinding()]
param()

Set-StrictMode -Version Latest
$ErrorActionPreference = "Stop"

$repoRoot = Split-Path -Parent $PSScriptRoot
Set-Location -LiteralPath $repoRoot

Write-Host "==> Validate WebExtension Manifests"
$manifestPaths = @("deploy/manifest.json", "source/manifest.json")
$manifestObjs = @{}
foreach ($relPath in $manifestPaths) {
    $fullPath = Join-Path $repoRoot $relPath
    if (-not (Test-Path -LiteralPath $fullPath)) {
        throw "Missing manifest: $relPath"
    }
    $raw = Get-Content -LiteralPath $fullPath -Raw -Encoding UTF8
    $json = ConvertFrom-Json $raw
    if ($json.manifest_version -ne 3) {
        throw "$relPath must declare manifest_version 3"
    }
    if ($json.name -ne "Sprucemarks") {
        throw "$relPath name mismatch: $($json.name)"
    }
    if (-not $json.version) {
        throw "$relPath missing version"
    }
    $manifestObjs[$relPath] = $json
    Write-Host "  OK: $relPath (v$($json.version), MV3)"
}
if ($manifestObjs["deploy/manifest.json"].version -ne $manifestObjs["source/manifest.json"].version) {
    throw "Manifest version mismatch: deploy=$($manifestObjs['deploy/manifest.json'].version) vs source=$($manifestObjs['source/manifest.json'].version)"
}

Write-Host "==> Validate Locales"
foreach ($locale in @("en", "zh_TW")) {
    foreach ($base in @("deploy", "source")) {
        $locPath = Join-Path $repoRoot "$base\_locales\$locale\messages.json"
        if (-not (Test-Path -LiteralPath $locPath)) {
            throw "Missing locale file: $base\_locales\$locale\messages.json"
        }
    }
}
Write-Host "  All locale files present (en, zh_TW) in deploy and source"

Write-Host "==> Validate Icons and Referenced Assets"
$deployManifest = ConvertFrom-Json (Get-Content -LiteralPath (Join-Path $repoRoot "deploy/manifest.json") -Raw -Encoding UTF8)
$iconCount = 0
foreach ($prop in $deployManifest.icons.PSObject.Properties) {
    $iconRel = $prop.Value
    $iconFull = Join-Path (Join-Path $repoRoot "deploy") $iconRel
    if (-not (Test-Path -LiteralPath $iconFull)) {
        throw "Icon not found: $iconRel"
    }
    $iconCount++
}
Write-Host "  All $iconCount icons present in deploy/images/icon"

$optionsPage = Join-Path (Join-Path $repoRoot "deploy") $deployManifest.options_ui.page
if (-not (Test-Path -LiteralPath $optionsPage)) {
    throw "Options page not found: $($deployManifest.options_ui.page)"
}
Write-Host "  Options page OK: $($deployManifest.options_ui.page)"

$serviceWorker = Join-Path (Join-Path $repoRoot "deploy") $deployManifest.background.service_worker
if (-not (Test-Path -LiteralPath $serviceWorker)) {
    throw "Service worker not found: $($deployManifest.background.service_worker)"
}
Write-Host "  Service worker OK: $($deployManifest.background.service_worker)"

Write-Host "==> Check JavaScript Syntax (Node.js)"
$nodeCmd = Get-Command node -ErrorAction SilentlyContinue
if ($null -ne $nodeCmd) {
    $jsFiles = Get-ChildItem -Recurse -Path (Join-Path $repoRoot "deploy"), (Join-Path $repoRoot "source") -Filter "*.js"
    foreach ($file in $jsFiles) {
        & $nodeCmd.Source --check $file.FullName
        if ($LASTEXITCODE -ne 0) {
            throw "Syntax error in $($file.FullName)"
        }
    }
    Write-Host "  $($jsFiles.Count) JS files syntax valid."
} else {
    Write-Host "  Node.js not detected; skipping node --check."
}

Write-Host "PRODUCT EXTENSION TESTS GREEN"
