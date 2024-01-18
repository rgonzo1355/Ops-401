#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 17 2024

# Purpose:File Encryption Script Part 2 of 3

from cryptography.fernet import Fernet  # Imports the Fernet class from the cryptography package
import os  # Imports the os module to interact with the operating system

def generate_key():
    key = Fernet.generate_key()  # Generates a new Fernet key
    with open("encryption_key.key", "wb") as key_file:  # Opens a file to save the key
        key_file.write(key)  # Writes the generated key to the file

def encrypt_file(filepath, key):
    fernet = Fernet(key)  # Creates a Fernet object using the provided key
    with open(filepath, "rb") as file:  # Opens the file to be encrypted in binary read mode
        file_data = file.read()  # Reads the file data
    encrypted_data = fernet.encrypt(file_data)  # Encrypts the file data
    with open(filepath, "wb") as file:  # Opens the file in binary write mode
        file.write(encrypted_data)  # Writes the encrypted data back to the file

def decrypt_file(filepath, key):
    fernet = Fernet(key)  # Creates a Fernet object using the provided key
    with open(filepath, "rb") as file:  # Opens the file to be decrypted in binary read mode
        encrypted_data = file.read()  # Reads the encrypted data from the file
    decrypted_data = fernet.decrypt(encrypted_data)  # Decrypts the data
    with open(filepath, "wb") as file:  # Opens the file in binary write mode
        file.write(decrypted_data)  # Writes the decrypted data back to the file

def encrypt_string(text, key):
    fernet = Fernet(key)  # Creates a Fernet object using the provided key
    encrypted_data = fernet.encrypt(text.encode())  # Encrypts the text after encoding it to bytes
    return encrypted_data.decode()  # Decodes the encrypted bytes back to a string and returns it

def decrypt_string(text, key):
    fernet = Fernet(key)  # Creates a Fernet object using the provided key
    decrypted_data = fernet.decrypt(text.encode())  # Decrypts the text after encoding it to bytes
    return decrypted_data.decode()  # Decodes the decrypted bytes back to a string and returns it

def list_files(directory):
    files_list = []  # Initializes an empty list to store file paths
    for root, _, files in os.walk(directory):  # Walks through the directory
        for file in files:  # Iterates through each file in the directory
            files_list.append(os.path.join(root, file))  # Appends the full file path to the list
    return files_list  # Returns the list of file paths

def main():
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):  # Checks if the key file does not exist
        generate_key()  # Generates a new key if the key file is not found

    key = open(key_file, "rb").read()  # Reads the encryption key from the key file

    while True:  # Starts an infinite loop for the user interface
        # Displays a menu for the user
        print("\033[94mSelect a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Encrypt a directory")
        print("6. Decrypt a directory")
        print("7. Exit\033[0m")

        mode = int(input("Enter the mode (1/2/3/4/5/6/7): "))  # Asks the user to select a mode

        # The following if-elif block executes the appropriate function based on the user's choice
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
            directory = input("Enter the path to the directory you want to encrypt: ")
            for filepath in list_files(directory):  # Iterates over all files in the specified directory
                encrypt_file(filepath, key)  # Encrypts each file in the directory
            print("\033[94mDirectory encrypted successfully.\033[0m")
        elif mode == 6:
            directory = input("Enter the path to the directory you want to decrypt: ")
            for filepath in list_files(directory):  # Iterates over all files in the specified directory
                decrypt_file(filepath, key)  # Decrypts each file in the directory
            print("\033[94mDirectory decrypted successfully.\033[0m")
        elif mode == 7:
            print("\033[94mGoodbye!\033[0m")  # Prints a goodbye message
            break  # Exits the while loop, thus ending the program
        else:
            print("\033[94mInvalid mode selection. Please select a valid mode (1/2/3/4/5/6/7).\033[0m")  # Handles invalid mode selection

if __name__ == "__main__":
    main()  # Executes the main function if the script is run as the main program


