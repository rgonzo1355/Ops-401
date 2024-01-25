#!/usr/bin/env python3
# Rodolfo Gonzalez
# 01-24-2024
# Challenge 11: Network Security Tool with Scapy 3 of 3

'''
This Python code combines ICMP ping and TCP port scanning functionalities into a single network scanner script. 
It prompts the user for a target IP address, start and end port numbers, performs an ICMP ping sweep to check host responsiveness, 
and then scans the specified range of ports, reporting their status. The code provides a comprehensive network scanning tool for the user.
References:
 https://chat.openai.com/share/9b839495-a143-457a-8cdc-813ff371c93c '''

####################################################################################################
# Import necessary libraries
####################################################################################################
from scapy.all import IP, TCP, sr1, ICMP  # Import classes for packet crafting and sending
from ipaddress import ip_network           # Import for IP address manipulation

####################################################################################################
# Function for TCP port scanning
####################################################################################################
def tcp_port_scanner(target_ip, port_range):
    """Scans a range of TCP ports on the target host."""

    for port in port_range:
        try:
            packet = IP(dst=target_ip) / TCP(dport=port, flags="S")  # Create a TCP SYN packet
            response = sr1(packet, timeout=1, verbose=0)         # Send the packet and capture response

            if response is None:
                print(f"Port {port}: Filtered or dropped")
            elif response.haslayer(TCP):
                if response[TCP].flags == 0x12:  # SYN-ACK received (port open)
                    print(f"\033[94mPort {port} is open\033[0m")
                    sr1(IP(dst=target_ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)  # Send RST to close connection
                elif response[TCP].flags == 0x14:  # RST received (port closed)
                    print(f"Port {port}: Closed")
        except Exception as e:
            print(f"Error scanning port {port}: {e}")

####################################################################################################
# Function for ICMP ping sweep
####################################################################################################
def icmp_ping_sweep(network):
    """Performs an ICMP ping sweep on a given network."""

    try:
        addresses = [str(ip) for ip in ip_network(network).hosts()]  # Generate list of IP addresses in the network
    except ValueError as e:
        print(f"Invalid network address: {e}")
        return

    online_hosts = 0
    for address in addresses:
        try:
            response = sr1(IP(dst=address)/ICMP(), timeout=1, verbose=0)  # Send ICMP echo request
            if response is None:
                print(f"{address} is down or unresponsive.")
            elif response.haslayer(ICMP):
                if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                    print(f"{address} is actively blocking ICMP traffic.")
                else:
                    print(f"{address} is responding.")
                    online_hosts += 1
        except Exception as e:
            print(f"Error pinging {address}: {e}")

    print(f"\n\033[94m{online_hosts} hosts are online.\033[0m")

####################################################################################################
# Main section
####################################################################################################
def main():
    """Main execution of the script."""

    try:
        target_ip = input("\033[94mEnter the target IP address: \033[0m")

        # Perform ICMP ping sweep first
        icmp_ping_sweep(target_ip)

        # If the host is responsive, proceed with port scanning
        if "is responding." in icmp_ping_sweep.output:
            while True:
                try:
                    port_range_input = input("\033[94mEnter the range of ports to scan (e.g., 22-55): \033[0m")
                    start_port, end_port = map(int, port_range_input.split("-"))

                    if start_port > end_port:
                        print("Start port must be less than end port. Please try again.")
                    else:
                        break
                except ValueError:
                    print("Input Error!")

            port_range = range(start_port, end_port + 1)

           

           
