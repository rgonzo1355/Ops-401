#!/usr/bin/python3
# Rodolfo Gonzalez
# 03-6-2024

# Challenge 43: Create a port scanner

'''This Python code prompts the user to input a host IP address and a port range. 
It then scans the specified range of ports on the provided host IP address to determine whether each port is open or closed, 
using multithreading for concurrent scanning and ANSI escape codes to colorize the output based on the port status (open or closed).'''
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
