# Prompt user for IP address
$IPAddress = Read-Host -Prompt "Enter the IP address to search for user names"

# Function to search for user names on the specified IP address
function SearchUserNames {
    param (
        [string]$IPAddress
    )

    try {
        # Attempt SSH connection to the specified IP address
        $plinkCommand = "echo y | plink.exe -ssh $IPAddress -l root cat /etc/passwd"
        $plinkOutput = Invoke-Expression -Command $plinkCommand

        # Parse user names from the output
        $userNames = $plinkOutput -split ":"
        $userNames = $userNames[0..($userNames.Count - 2)]

        # Display the user names
        Write-Host "User names found on $IPAddress:"
        $userNames | ForEach-Object {
            Write-Host $_
        }
    }
    catch {
        Write-Host "An error occurred while searching for user names on $IPAddress: $_" -ForegroundColor Red
    }
}

# Call the function to search for user names
SearchUserNames -IPAddress $IPAddress
