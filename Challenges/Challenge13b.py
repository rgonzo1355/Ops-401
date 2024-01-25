
#!/usr/bin/env python3
# Rodolfo Gonzalez
# 01-24-2024
# Challenge 11: Network Security Tool with Scapy 3 of 3

''' This code imports necessary libraries: Scapy for network packet manipulation and ipaddress for IP address handling.
Defines a function for TCP port scanning:
Sends TCP SYN probes to specified ports on the target host.
Analyzes responses to determine port status (open, closed, filtered).
Defines a function for ICMP ping sweep:
Sends ICMP echo requests to hosts within a given network.
Identifies which hosts are online, offline, or blocking ICMP traffic.
Main execution:
Prompts the user for a target IP address.
Performs an ICMP ping sweep on the target.
If the target is responsive, prompts for a port range to scan.
Initiates TCP port scanning on the specified port range.
Prints results of both ping sweep and port scanning to the screen.
References:
 https://chat.openai.com/share/9b839495-a143-457a-8cdc-813ff371c93c 
 https://g.co/bard/share/cf1c27b02301
 https://g.co/bard/share/cf1c27b02301
 https://chat.openai.com/share/5167902b-6679-4ab5-8f61-15a53d583db3
 '''

from scapy.all import IP, TCP, sr1, ICMP
from ipaddress import ip_network

def tcp_port_scanner(target_ip, port_range):
    open_ports = []

    for port in port_range:
        try:
            packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
            response = sr1(packet, timeout=2, verbose=0)

            if response is None:
                print(f"Port {port}: Filtered or dropped")
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x12:
                    open_ports.append(port)
                    sr1(IP(dst=target_ip) / TCP(dport=port, flags="R"), timeout=1, verbose=0)
                elif response[TCP].flags == 0x14:
                    print(f"Port {port} is closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

    return open_ports

def main():
    try:
        target_ip = input("Enter the target IP address: ")

        icmp_response = sr1(IP(dst=target_ip) / ICMP(), timeout=2, verbose=0)

        if icmp_response is None:
            print(f"{target_ip} is down or unresponsive.")
        elif icmp_response.haslayer(ICMP):
            if icmp_response[ICMP].type == 3 and icmp_response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                print(f"{target_ip} is actively blocking ICMP traffic.")
            else:
                print(f"{target_ip} is responding.")
                port_range_input = input("Enter the range of ports to scan (e.g., 22-55): ")
                start_port, end_port = map(int, port_range_input.split("-"))

                if start_port > end_port:
                    print("Start port must be less than end port. Please try again.")
                else:
                    port_range = range(start_port, end_port + 1)
                    open_ports = tcp_port_scanner(target_ip, port_range)

                    if open_ports:
                        print("Open ports:")
                        for port in open_ports:
                            print(port)
                    else:
                        print("No open ports found.")

    except KeyboardInterrupt:
        print("Scanning canceled by user.")
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    main()
