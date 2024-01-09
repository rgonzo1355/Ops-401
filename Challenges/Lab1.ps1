# Script Name:               Ops Lab 01: Powershell AD Automation
# Author:                    Rodolfo Gonzalez
# Date:                      01/08/2024      

# Purpose: This PowerShell script automatically sets up a screen lock on Windows 10 after a period of time.
# https://chat.openai.com/share/d332a0bf-301e-4283-afc8-ac3697ce095d.

# This sets the time of inactivity in seconds before the screen locks (300 sec = 5 minutes).
$InactivityLimit = 300

# The registry path where the screen lock settings are stored.
$registryPath = "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop"
$propertyName = "ScreenSaveTimeOut" # Name of the property to be set.
$propertyValue = $InactivityLimit # Value of the property (time limit).

# Starts a 'Try' block to handle potential errors.
Try {
    # Checks if the registry path exists; if it does not, the script creates it.
    if (!(Test-Path $registryPath)) {
        New-Item -Path $registryPath -Force | Out-Null
    }

    # Sets the screen save timeout value in the registry.
    Set-ItemProperty -Path $registryPath -Name $propertyName -Value $propertyValue

    # Activates the screen saver feature.
    Set-ItemProperty -Path $registryPath -Name "ScreenSaveActive" -Value "1"

    # Prints a message confirming successful registry update.
    Write-Host "Registry updated successfully."
} Catch {
    Write-Host "Error: $_"
}

Get-ItemProperty -Path "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop" -Name "ScreenSaveTimeOut"
Get-ItemProperty -Path "HKCU:\SOFTWARE\Policies\Microsoft\Windows\Control Panel\Desktop" -Name "ScreenSaveActive"
