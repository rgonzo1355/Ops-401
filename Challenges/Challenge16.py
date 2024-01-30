#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 29 2024

# Purpose: Challenge 16: Automate Brute Force Wordlis Attack Tool 1 of 3

import time
import os

# Set the path to the RockYou.txt file
ROCKYOU_PATH = os.path.expanduser("~/Documents/rockyou.txt")

##################### === Function for Offensive Mode ===###################
def offensive_mode():
    try:
        # Prompt for the number of lines to process
        lines_to_read = int(input("Enter the number of lines to process: "))

        # Open the wordlist file in binary mode and read specified number of lines
        with open(ROCKYOU_PATH, 'rb') as wordlist_file:
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

        # Display search result
        if found:
            print("\033[91mYour word IS in the word list.\033[0m]")       
        else:
            print("\033[92mYour word is NOT in the word list.\033[0m]")

    except FileNotFoundError:
        print("Word list file not found.")
    except KeyboardInterrupt:
        print("Operation aborted by the user.")

##################### === Main program ===###################
if __name__ == "__main__":
    while True:
        print("\033[35mSelect a mode:\033[0m]")
        print("1. Offensive; Dictionary Iterator")
        print("2. Defensive; Password Recognized")
        print("3. Exit")

        mode = input("\033[35mEnter mode (1, 2, or 3 to exit): \033[0m")

        try:
            if mode == "1":
                # Run Offensive Mode
                offensive_mode()
            elif mode == "2":
                # Run Defensive Mode
                defensive_mode()
            elif mode == "3":
                print("\033[340mExiting the program. Goodbye!\033[0m")
                break  # Exit the loop and end the program
            else:
                print("Invalid mode. Please select 1, 2, or 3.")

        except KeyboardInterrupt:
            print("Operation aborted by the user.")

##################### ===End of Code ===###################

