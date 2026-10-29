# Read-only export. Requires operator-authorised tenant access and Microsoft Graph modules.
# Real tenant data is sensitive. Do not commit generated CSV reports.
[CmdletBinding()]
param(
    [string] $OutputPath = "./local-output/tenant_users.csv"
)

$ErrorActionPreference = "Stop"
Import-Module Microsoft.Graph.Authentication -ErrorAction Stop
Import-Module Microsoft.Graph.Users -ErrorAction Stop

# No write permissions are requested. Sign-in details require Entra licensing
# and the AuditLog.Read.All permission, as documented by Microsoft.
Connect-MgGraph -Scopes @("User.Read.All", "AuditLog.Read.All") -NoWelcome
try {
    $users = Get-MgUser -All -Property @(
        "id", "displayName", "userPrincipalName",
        "accountEnabled", "assignedLicenses", "signInActivity"
    )
    $records = foreach ($user in $users) {
        $lastSuccess = ""
        if ($null -ne $user.SignInActivity -and
            $null -ne $user.SignInActivity.LastSuccessfulSignInDateTime) {
            $lastSuccess = ([datetimeoffset] $user.SignInActivity.LastSuccessfulSignInDateTime).ToString("o")
        }
        $skuIds = @(
            foreach ($license in $user.AssignedLicenses) {
                if ($null -ne $license.SkuId) { $license.SkuId.ToString() }
            }
        )
        [pscustomobject]@{
            user_id = $user.Id
            display_name = $user.DisplayName
            user_principal_name = $user.UserPrincipalName
            account_enabled = ([bool] $user.AccountEnabled).ToString().ToLowerInvariant()
            last_successful_sign_in = $lastSuccess
            assigned_licenses = ($skuIds -join ";")
        }
    }
    $destination = $ExecutionContext.SessionState.Path.GetUnresolvedProviderPathFromPSPath($OutputPath)
    $folder = Split-Path -Parent $destination
    if (-not (Test-Path -LiteralPath $folder)) {
        New-Item -ItemType Directory -Path $folder -Force | Out-Null
    }
    $records | Export-Csv -Path $destination -NoTypeInformation -Encoding utf8
    Write-Host "Exported $(@($records).Count) user records to $destination"
}
finally {
    Disconnect-MgGraph -ErrorAction SilentlyContinue | Out-Null
}
