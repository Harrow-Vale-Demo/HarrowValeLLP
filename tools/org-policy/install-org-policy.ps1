<#
.SYNOPSIS
  Applies the Harrow & Vale plugin policy as Claude Code managed settings.

.DESCRIPTION
  Writes managed-settings.json into the Windows policy registry key that Claude
  Code reads. This is the mechanism a real IT department uses via Group Policy or
  Intune; running it per-user needs no administrator rights, which is what makes
  it usable for a demo on three ordinary laptops.

  Managed settings sit at the TOP of Claude Code's precedence order. A plugin
  named in enabledPlugins is force-enabled and a user cannot turn it off, which
  is the point: the firm decides which skills its lawyers use.

  Default target is HKCU (current user only, no admin rights, easily reversed).
  Pass -Machine for the whole machine, which does require an elevated shell.

.PARAMETER Machine
  Write to HKLM instead of HKCU. Requires an elevated PowerShell session.

.PARAMETER Uninstall
  Remove the policy key.

.PARAMETER Show
  Print the policy currently in effect and exit without changing anything.

.EXAMPLE
  .\install-org-policy.ps1
  Applies the policy for the current user.

.EXAMPLE
  .\install-org-policy.ps1 -Show
  Shows what is currently applied.

.EXAMPLE
  .\install-org-policy.ps1 -Uninstall
  Removes it again.

.NOTES
  Restart Claude Code after applying. Verify with:  claude doctor
#>
[CmdletBinding()]
param(
    [switch]$Machine,
    [switch]$Uninstall,
    [switch]$Show
)

$ErrorActionPreference = 'Stop'

if ($Machine) {
    $root = 'HKLM:\SOFTWARE\Policies\ClaudeCode'
    $scope = 'machine (all users)'
} else {
    $root = 'HKCU:\SOFTWARE\Policies\ClaudeCode'
    $scope = 'current user'
}

if ($Show) {
    if (Test-Path $root) {
        $existing = (Get-ItemProperty -Path $root -Name 'Settings' -ErrorAction SilentlyContinue).Settings
        if ($existing) {
            Write-Host "Policy in effect for $scope :" -ForegroundColor Cyan
            Write-Host $existing
        } else {
            Write-Host "Key $root exists but has no Settings value." -ForegroundColor Yellow
        }
    } else {
        Write-Host "No policy applied for $scope." -ForegroundColor Yellow
    }
    return
}

if ($Uninstall) {
    if (Test-Path $root) {
        Remove-Item -Path $root -Recurse -Force -Confirm:$false
        Write-Host "Removed Claude Code plugin policy for $scope." -ForegroundColor Green
    } else {
        Write-Host "Nothing to remove - no policy applied for $scope." -ForegroundColor Yellow
    }
    Write-Host "Restart Claude Code for this to take effect."
    return
}

$policyFile = Join-Path $PSScriptRoot 'managed-settings.json'
if (-not (Test-Path $policyFile)) {
    throw "Cannot find $policyFile"
}

# Validate before writing: a malformed policy is worse than none.
$raw = Get-Content -Path $policyFile -Raw
try {
    $parsed = $raw | ConvertFrom-Json
} catch {
    throw "managed-settings.json is not valid JSON: $($_.Exception.Message)"
}

if (-not $parsed.extraKnownMarketplaces) {
    throw "managed-settings.json declares no extraKnownMarketplaces; refusing to apply an empty policy."
}

# Compact the JSON so it survives the registry as a single REG_SZ value.
$compact = $parsed | ConvertTo-Json -Depth 20 -Compress

if (-not (Test-Path $root)) {
    New-Item -Path $root -Force | Out-Null
}
New-ItemProperty -Path $root -Name 'Settings' -Value $compact -PropertyType String -Force | Out-Null

Write-Host "Applied Claude Code plugin policy for $scope." -ForegroundColor Green
Write-Host "  key        $root"
Write-Host "  marketplaces $($parsed.extraKnownMarketplaces.Count)"
Write-Host "  plugins      $($parsed.enabledPlugins.Count) force-enabled"
Write-Host ""
Write-Host "Restart Claude Code, then verify with:" -ForegroundColor Cyan
Write-Host "  claude doctor"
Write-Host "  claude plugin list"
