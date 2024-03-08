#!/usr/bin/python3
# Rodolfo Gonzalez
# 03-5-2024

# Ops Challenge - Attack Tools Part 2 of 3

"""This Python script implements a custom Nmap scanner tool. It prompts the user to input an IP address to scan and choose from three scan types: 
SYN ACK Scan, UDP Scan, or TCP Connect Scan. After specifying a port range, it executes the selected scan type using the python-nmap library. 
Finally, it displays scan results such as Nmap version, IP status, and open ports, with successful results highlighted in green.
You will need to make sure that following are installed: 
-sudo apt-get install python3-pip
-sudo pip3 install python-nmap
-You will also need sudo.
"""


import nmap
from colorama import Fore, Style

scanner = nmap.PortScanner()

print(Fore.MAGENTA + "Nmap Automation Tool" + Style.RESET_ALL)
print("--------------------")

ip_addr = input("Enter the IP address to scan: ")
print("The IP you entered is:", ip_addr)

resp = input(Fore.MAGENTA + """\nSelect scan to execute:
                1) SYN ACK Scan
                2) UDP Scan
                3) TCP Connect Scan\n""" + Style.RESET_ALL)
print(Fore.MAGENTA + "You have selected option:", resp + Style.RESET_ALL)

port_range = input("Enter port range (e.g., 1-100): ")

if resp == '1':
    print(Fore.GREEN + "Nmap Version:", '.'.join(map(str, scanner.nmap_version())) + Style.RESET_ALL)
    scanner.scan(ip_addr, port_range, '-v -sS')
    print(scanner.scaninfo())
    print(Fore.GREEN + "IP Status:", scanner[ip_addr].state() + Style.RESET_ALL)
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print(Fore.GREEN + "Open Ports:", list(scanner[ip_addr]['tcp'].keys()) + Style.RESET_ALL)
    else:
        print(Fore.RED + "No open TCP ports found." + Style.RESET_ALL)
elif resp == '2':
    print(Fore.GREEN + "Nmap Version:", '.'.join(map(str, scanner.nmap_version())) + Style.RESET_ALL)
    scanner.scan(ip_addr, port_range, '-v -sU')
    print(scanner.scaninfo())
    print(Fore.GREEN + "IP Status:", scanner[ip_addr].state() + Style.RESET_ALL)
    print(scanner[ip_addr].all_protocols())
    if 'udp' in scanner[ip_addr]:
        print(Fore.GREEN + "Open Ports:", list(scanner[ip_addr]['udp'].keys()) + Style.RESET_ALL)
    else:
        print(Fore.RED + "No open UDP ports found." + Style.RESET_ALL)
elif resp == '3':
    print(Fore.GREEN + "Nmap Version:", '.'.join(map(str, scanner.nmap_version())) + Style.RESET_ALL)
    scanner.scan(ip_addr, port_range, '-v -sT')
    print(scanner.scaninfo())
    print(Fore.GREEN + "IP Status:", scanner[ip_addr].state() + Style.RESET_ALL)
    print(scanner[ip_addr].all_protocols())
    if 'tcp' in scanner[ip_addr]:
        print(Fore.GREEN + "Open Ports:", list(scanner[ip_addr]['tcp'].keys()) + Style.RESET_ALL)
    else:
        print(Fore.RED + "No open TCP ports found." + Style.RESET_ALL)
else:
    print(Fore.RED + "Please enter a valid option" + Style.RESET_ALL)
