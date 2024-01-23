#!/usr/bin/env python3
# Rodolfo Gonzalez
# 01-22-2024
# Challenge 11: Network Security Tool with Scapy 1 of 3

# https://chat.openai.com/share/68411f65-6910-4701-a3fa-65fba8ccc5cb

# Importing the necessary Scapy classes
from scapy.all import IP, TCP, sr1

def tcp_port_scanner(target_ip, port_range):
    # Iterating over the specified port range
    for port in port_range:
        # Creating a TCP packet with the SYN flag, targeted at the specified IP and port
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")

        # Sending the packet and waiting for a response with a timeout of 1 second
        response = sr1(packet, timeout=1, verbose=0)

        # If no response is received, it's assumed the port is filtered or dropped
        if response is None:
            print(f"Port {port}: Filtered or dropped")
        # Checking if the response includes TCP layer information
        elif response.haslayer(TCP):
            # If SYN-ACK (0x12) is received, the port is open
            if response[TCP].flags == 0x12:
                print(f"\033[94mPort {port} is open\033[0m")
                # Sending a RST packet to close the connection gracefully
                sr1(IP(dst=target_ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
            # If RST-ACK (0x14) is received, the port is closed
            elif response[TCP].flags == 0x14:
                print(f"Port {port}: Closed")

def main():
    # Prompting for the target IP address
    target_ip = input("Enter the target IP address: ")

    # Prompting for the start and end of the port range
    start_port = int(input("Enter the start port: "))
    end_port = int(input("Enter the end port: "))

    # Validating that the start port is less than the end port
    if start_port > end_port:
        print("Start port must be less than end port. Please try again.")
        return

    # Running the scanner on the specified port range
    tcp_port_scanner(target_ip, range(start_port, end_port + 1))

# Ensuring the script only runs when executed directly (not imported)
if __name__ == "__main__":
    main()
