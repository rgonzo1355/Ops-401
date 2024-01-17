#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 16 2024

# Purpose:File Encryption Script Part 1 of 3

"""The purpose of this code is to create a Python script that allows users to perform file encryption and decryption using the cryptography library. 
It provides a user-friendly menu-based interface with options to encrypt files, decrypt files, encrypt messages, decrypt messages, and exit the program.
 The script generates an encryption key, ensures secure data handling, and displays answers in blue for clarity.
 You must have or do: pip install cryptography==3.1.1
You can use file "Encrypted.txt" to encrypt and decrypt.
References:
https://pypi.org/project/cryptography/
https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
https://www.youtube.com/watch?v=4_s9lOuUpZ4
https://www.youtube.com/watch?v=zWNA2ThkVT4
https://chat.openai.com/share/40f73039-a743-4366-9bfc-3b96c3081daa
"""

# Import necessary modules from the cryptography library and the os module for file operations.
from cryptography.fernet import Fernet
import os

# Function to generate a new encryption key and save it to a file.
def generate_key():
    # Generate a new Fernet key.
    key = Fernet.generate_key()
    # Save the key to a file named "encryption_key.key" in binary mode.
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

# Function to encrypt a file given its filepath.
def encrypt_file(filepath, key):
    # Create a Fernet encryption object with the provided key.
    fernet = Fernet(key)
    # Open the target file in binary read mode.
    with open(filepath, "rb") as file:
        # Read the file data.
        file_data = file.read()
    # Encrypt the file data.
    encrypted_data = fernet.encrypt(file_data)
    # Open the same file in binary write mode and replace its content with the encrypted data.
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

# Function to decrypt a file given its filepath.
def decrypt_file(filepath, key):
    # Create a Fernet decryption object with the provided key.
    fernet = Fernet(key)
    # Open the target file in binary read mode.
    with open(filepath, "rb") as file:
        # Read the encrypted file data.
        encrypted_data = file.read()
    # Decrypt the file data.
    decrypted_data = fernet.decrypt(encrypted_data)
    # Open the same file in binary write mode and replace its content with the decrypted data.
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

# Function to encrypt a string.
def encrypt_string(text, key):
    # Create a Fernet encryption object with the provided key.
    fernet = Fernet(key)
    # Encrypt the string text after encoding it to bytes.
    encrypted_data = fernet.encrypt(text.encode())
    # Decode the encrypted data to get a string representation.
    return encrypted_data.decode()

# Function to decrypt a string.
def decrypt_string(text, key):
    # Create a Fernet decryption object with the provided key.
    fernet = Fernet(key)
    # Decrypt the string text after encoding it to bytes.
    decrypted_data = fernet.decrypt(text.encode())
    # Decode the decrypted data to get the original string.
    return decrypted_data.decode()

# Main function to control the program flow.
def main():
    # Check if the encryption key file exists. If not, generate a new key.
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):
        generate_key()

    # Read the encryption key from the key file.
    key = open(key_file, "rb").read()

    while True:
        # Display a menu for the user to select a mode.
        print("\033[94mSelect a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Exit\033[0m")

        # Prompt the user to enter the desired mode (1/2/3/4/5).
        mode = int(input("Enter the mode (1/2/3/4/5): "))

        # Based on the selected mode, perform the corresponding action.
        if mode == 1:
            filepath = input("Enter the path to the file you want to encrypt: ")
            encrypt_file(filepath, key)
            print("\033[94mFile encrypted successfully.\033[0m")
        elif mode == 2:
            filepath = input("Enter the path to the file you want to decrypt: ")
            decrypt_file(filepath, key)
            print("\033[94mFile decrypted successfully.\033[0m")
        elif mode == 3:
            text = input("Enter the message you want to encrypt: ")
            encrypted_text = encrypt_string(text, key)
            print("\033[94mEncrypted message:", encrypted_text, "\033[0m")
        elif mode == 4:
            text = input("Enter the encrypted message: ")
            decrypted_text = decrypt_string(text, key)
            print("\033[94mDecrypted message:", decrypted_text, "\033[0m")
        elif mode == 5:
            print("\033[94mGoodbye!\033[0m")
            break
        else:
            print("\033[94mInvalid mode selection. Please select a valid mode (1/2/3/4/5).\033[0m")

# Entry point of the script.
if __name__ == "__main__":
    main()
