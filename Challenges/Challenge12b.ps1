# Import the necessary modules
Import-Module -Name NetSecurity -Force

# Define a function to perform TCP port scanning
function Perform-TcpPortScan {
    param (
        [string]$targetIp,
        [int]$startPort,
        [int]$endPort
    )

    $onlinePorts = @()

    for ($port = $startPort; $port -le $endPort; $port++) {
        $tcpClient = New-Object System.Net.Sockets.TcpClient
        $connectionResult = $tcpClient.BeginConnect($targetIp, $port, $null, $null)
        $isPortOpen = $connectionResult.AsyncWaitHandle.WaitOne(1000, $false)

        if ($isPortOpen) {
            $onlinePorts += $port
            Write-Host "Port $port is open"
            $tcpClient.Close()
        } else {
            Write-Host "Port $port is closed"
        }
    }

    return $onlinePorts
}

# Define a function to perform ICMP ping sweep
function Perform-IcmpPingSweep {
    param (
        [string]$subnet
    )

    try {
        # Get all host IP addresses in the specified subnet
        $addresses = 1..254 | ForEach-Object {
            $subnet + $_
        }

        $onlineHosts = @()

        foreach ($address in $addresses) {
            $pingResult = Test-Connection -ComputerName $address -Count 1 -ErrorAction SilentlyContinue
            if ($pingResult) {
                $onlineHosts += $address
                Write-Host "$address is online"
            } else {
                Write-Host "$address is offline"
            }
        }

        Write-Host ""
        Write-Host ("{0} hosts are online." -f $onlineHosts.Count)
    } catch {
        Write-Host "An error occurred: $_"
    }
}

# Main menu
Write-Host "Select mode"
Write-Host "1- TCP Port Scanner"
Write-Host "2- ICMP Ping Sweep"

# Prompt for mode selection
$mode = Read-Host "Enter the mode (1 or 2)"

if ($mode -eq '1') {
    $targetIp = Read-Host "Enter the target IP address"
    $startPort = Read-Host "Enter the start port"
    $endPort = Read-Host "Enter the end port"

    $onlinePorts = Perform-TcpPortScan -targetIp $targetIp -startPort $startPort -endPort $endPort
    Write-Host ("{0} ports are open: {1}" -f $onlinePorts.Count, $onlinePorts -join ", ")
} elseif ($mode -eq '2') {
    $network = Read-Host "Enter the network address with CIDR (e.g., 192.168.1.0/24)"
    $subnet = ($network -split "/")[0] + "."

    Perform-IcmpPingSweep -subnet $subnet
} else {
    Write-Host "Invalid choice. Please enter 1 or 2."
}
