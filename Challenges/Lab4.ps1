'''This challenge is taken straigh out of Brandon Wilbur's git page it is to be used in Lab 4 from Ops 401.

The script "SYSTEM HARDENING" appears to be designed to configure a Windows 10 Workstation with intentional vulnerabilities that can be remediated through system hardening. Here's a summary of what the script does:
Disable Windows Defender: The script begins by disabling Windows Defender's real-time monitoring and making changes in the Windows Defender registry to disable anti-spyware features. It also adds an exclusion path for Windows Defender.
Add User: It creates a new local user named 'Zuko' with the password 'R0cks!' and adds this user to the 'Administrators' group, granting administrative privileges.
Download File for AV Detection: The script downloads a file (ncat-portable-5.59BETA1.zip) from 'http://nmap.org' and saves it as 'nc.zip' in the user's AppData directory. It then extracts the contents of 'nc.zip' to 'C:\Program Files\Windows.' This action may be intended to simulate a potential threat for antivirus detection.
Configure Local Security Policy: The script mentions a step for configuring a local security policy but does not provide the actual policy settings. Instead, it gives instructions on obtaining a preconfigured security policy and converting it into a base64 string.
UAC (User Account Control): The script makes changes related to User Account Control but does not specify the details of these changes.
Restart Computer: The script concludes by restarting the computer.

https://github.com/champlain-cyberlabs/cyberlabs/blob/main/windows-scripts/system-hardening/system-hardening.ps1 '''