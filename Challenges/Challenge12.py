#!/usr/bin/env python3
# Rodolfo Gonzalez
# 01-23-2024
# Challenge 11: Network Security Tool with Scapy 2 of 3

"""The code is a network security tool featuring a TCP Port Scanner and an ICMP Ping Sweep. The Port Scanner evaluates ports' status (open, closed,
 or filtered/dropped) on a specified IP address,
 while the Ping Sweep identifies active or ICMP-blocking hosts within a network range.
 References:
 https://chat.openai.com/share/9b839495-a143-457a-8cdc-813ff371c93c """

# Importing the necessary Scapy classes
from scapy.all import IP, TCP, sr1, ICMP, sr
from ipaddress import ip_network

def tcp_port_scanner(target_ip, port_range):
    for port in port_range:
        packet = IP(dst=target_ip) / TCP(dport=port, flags="S")
        response = sr1(packet, timeout=1, verbose=0)

        if response is None:
            print(f"Port {port}: Filtered or dropped")
        elif response.haslayer(TCP):
            if response[TCP].flags == 0x12:
                print(f"\033[94mPort {port} is open\033[0m")
                sr1(IP(dst=target_ip)/TCP(dport=port, flags="R"), timeout=1, verbose=0)
            elif response[TCP].flags == 0x14:
                print(f"Port {port}: Closed")

def icmp_ping_sweep(network):
    addresses = [str(ip) for ip in ip_network(network).hosts()]
    online_hosts = 0

    for address in addresses:
        response = sr1(IP(dst=address)/ICMP(), timeout=1, verbose=0)
        if response is None:
            print(f"{address} is down or unresponsive.")
        elif response.haslayer(ICMP):
            if response[ICMP].type == 3 and response[ICMP].code in [1, 2, 3, 9, 10, 13]:
                print(f"{address} is actively blocking ICMP traffic.")
            else:
                print(f"{address} is responding.")
                online_hosts += 1
        else:
            print(f"{address} is down or unresponsive.")

    print(f"\n{online_hosts} hosts are online.")

def main():
    mode = input("Select mode 1- TCP Port Scanner\n            2- ICMP Ping Sweep ")
    
    if mode == '1':
        target_ip = input("Enter the target IP address: ")
        start_port = int(input("Enter the start port: "))
        end_port = int(input("Enter the end port: "))
        if start_port > end_port:
            print("Start port must be less than end port. Please try again.")
            return
        tcp_port_scanner(target_ip, range(start_port, end_port + 1))

    elif mode == '2':
        network = input("Enter the network address with CIDR (e.g., 192.168.1.0/24): ")
        icmp_ping_sweep(network)

    else:
        print("Invalid choice. Please enter 1 or 2.")

if __name__ == "__main__":
    main()
