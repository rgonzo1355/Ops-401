# Script Name:               Ops Lab 01: Powershell AD Automation
# Author:                    Rodolfo Gonzalez
# Date:                      01/08/2024      

# Purpose: This PowerShell script automatically sets up a screen lock on Windows 10 after a period of time.

# Parameters
param (
    [int]$InactivityLimit = 350,   # Time of inactivity in seconds before the screen locks (default: 350 seconds)
    [string]$RegistryPath = "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop",  # Registry path
    [string]$PropertyName = "ScreenSaveTimeOut",  # Name of the property to be set
    [string]$BackupPath = "C:\Backup\ScreenLockRegistryBackup.reg"  # Backup file path
)

# Error Handling
Try {
    # Check if the registry path exists; if not, create it
    if (!(Test-Path $RegistryPath)) {
        New-Item -Path $RegistryPath -Force | Out-Null
    }

    # Backup existing registry value
    Export-Registry -Path $RegistryPath -BackupPath $BackupPath

    # Enable the screensaver
    Set-ItemProperty -Path $RegistryPath -Name "ScreenSaveActive" -Value "1"

    # Set the screen lock timeout
    Set-ItemProperty -Path $RegistryPath -Name $PropertyName -Value $InactivityLimit

    Write-Host "Screen lock settings successfully configured."
} 
Catch {
    Write-Host "Error: $($Error[0])"
    # You can add more specific error handling and logging here
}

# Function to export registry keys
function Export-Registry {
    param (
        [string]$Path,
        [string]$BackupPath
    )
    try {
        Write-Host "Backing up registry key to $BackupPath"
        Export-RegistryKey -Path $Path -LiteralPath $BackupPath -Force
    }
    catch {
        Write-Host "Error exporting registry key: $($_.Exception.Message)"
    }
}

