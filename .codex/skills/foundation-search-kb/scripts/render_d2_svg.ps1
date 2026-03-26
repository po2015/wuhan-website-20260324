param(
    [Parameter(Mandatory = $true)]
    [string]$InputPath,

    [string]$OutputPath,

    [ValidateSet('dagre', 'elk')]
    [string]$Layout = 'elk',

    [int]$Pad = 48
)

$resolvedInput = (Resolve-Path -LiteralPath $InputPath).Path
if (-not $OutputPath) {
    $OutputPath = [System.IO.Path]::ChangeExtension($resolvedInput, '.svg')
}

$resolvedOutput = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputPath)
$outputDir = Split-Path -Parent $resolvedOutput
if ($outputDir -and -not (Test-Path -LiteralPath $outputDir)) {
    New-Item -ItemType Directory -Path $outputDir -Force | Out-Null
}

$d2Command = Get-Command d2 -ErrorAction SilentlyContinue
$d2Path = if ($d2Command) { $d2Command.Source } elseif (Test-Path 'C:\Program Files\D2\d2.exe') { 'C:\Program Files\D2\d2.exe' } else { $null }

if (-not $d2Path) {
    throw "D2 CLI not found. Install Terrastruct.D2 or add d2.exe to PATH."
}

$previousDebug = $env:DEBUG
if ($previousDebug -and $previousDebug -notin @('0', '1', 'false', 'true')) {
    $env:DEBUG = '0'
}

& $d2Path --layout $Layout --pad $Pad $resolvedInput $resolvedOutput
$renderExitCode = $LASTEXITCODE

if ($null -ne $previousDebug) {
    $env:DEBUG = $previousDebug
} else {
    Remove-Item Env:DEBUG -ErrorAction SilentlyContinue
}

if ($renderExitCode -ne 0) {
    throw "D2 render failed with exit code $renderExitCode."
}

Write-Output $resolvedOutput
