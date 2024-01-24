import logging
from scapy.all import IP, TCP, sr1, ICMP
from ipaddress import ip_network

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def validate_port_range(start_port, end_port):
    try:
        # Validate and convert start and end port numbers
        start_port, end_port = int(start_port), int(end_port)
        if start_port > end_port or start_port < 1 or end_port > 65535:
            raise ValueError("Invalid port range")
        return start_port, end_port
    except ValueError:
        raise ValueError("Invalid port numbers")

def tcp_port_scanner(target_ip, start_port, end_port):
    # Validate port range
    start_port, end_port = validate_port_range(start_port, end_port)
    online_ports = []

    # Loop through ports and scan
    for port in range(start_port, end_port + 1):
        try:
            packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
            response = sr1(packet, timeout=1, verbose=0)
            if response is None:
                logger.info(f"Port {port}: Filtered or dropped")
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x12:
                    logger.info(f"Port {port} is open")
                    sr1(IP(dst=target_ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
                    online_ports.append(port)
                elif response[TCP].flags == 0x14:
                    logger.info(f"Port {port}: Closed")
        except Exception as e:
            logger.error(f"Error scanning port {port}: {e}")

    return online_ports

def validate_network(network):
    try:
        # Validate and convert network address
        return str(ip_network(network).network_address)
    except ValueError as e:
        raise ValueError(f"Invalid network address: {e}")

def icmp_ping_sweep(network):
    # Validate network address
    network = validate_network(network)
    online_hosts = []

    # Loop through hosts and ping
    for address in ip_network(network).hosts():
        try:
            response = sr1(IP(dst=str(address)) / ICMP(), timeout=1, verbose=0)
            if response is None:
                logger.info(f"{address} is down or unresponsive.")
            elif response.haslayer(ICMP):
                if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                    logger.info(f"{address} is actively blocking ICMP traffic.")
                else:
                    logger.info(f"{address} is responding.")
                    online_hosts.append(str(address))
        except Exception as e:
            logger.error(f"Error pinging {address}: {e}")

    return online_hosts

def main():
    try:
        mode = input("Select mode 1- TCP Port Scanner\n            2- ICMP Ping Sweep ")

        if mode == '1':
            target_ip = input("Enter the target IP address: ")
            start_port = input("Enter the start port: ")
            end_port = input("Enter the end port: ")
            online_ports = tcp_port_scanner(target_ip, start_port, end_port)
            logger.info(f"{len(online_ports)} ports are open: {online_ports}")

        elif mode == '2':
            network = input("Enter the network address with CIDR (e.g., 192.168.1.0/24): ")
            online_hosts = icmp_ping_sweep(network)
            logger.info(f"{len(online_hosts)} hosts are online: {online_hosts}")

        else:
            logger.error("Invalid choice. Please enter 1 or 2.")
    except Exception as e:
        logger.error(f"An error occurred: {e}")

if __name__ == "__main__":
    main()