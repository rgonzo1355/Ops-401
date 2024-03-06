#!/usr/bin/python3

import socket
import concurrent.futures

# ANSI escape codes for colors
GREEN = '\033[92m'
RED = '\033[91m'
RESET = '\033[0m'

def scan_port(hostip, port):
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sockmod:
            sockmod.settimeout(1)  # Set a timeout value
            result = sockmod.connect_ex((hostip, port))
            if result == 0:
                print(f"Port {port} {GREEN}open{RESET}")
            else:
                print(f"Port {port} {RED}closed{RESET}")
    except socket.error as e:
        print(f"Error while scanning port {port}: {e}")

def portScanner(hostip, start_port, end_port):
    print(f"Scanning ports {start_port} to {end_port} on host {hostip}...")
    with concurrent.futures.ThreadPoolExecutor() as executor:
        futures = [executor.submit(scan_port, hostip, port) for port in range(start_port, end_port + 1)]
        concurrent.futures.wait(futures)

if __name__ == "__main__":
    hostip = input("Enter the host IP: ")  # Collect host IP from the user
    port_range = input("Enter the port range (start-end): ")  # Collect port range from the user

    start_port, end_port = map(int, port_range.split('-'))

    portScanner(hostip, start_port, end_port)
