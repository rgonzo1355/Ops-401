#!/usr/bin/env python3

# Rodolfo Gonzalez
# January 17 2024

# Purpose:File Encryption Script Part 2 of 3

from cryptography.fernet import Fernet
import os

def generate_key():
    key = Fernet.generate_key()
    with open("encryption_key.key", "wb") as key_file:
        key_file.write(key)

def encrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        file_data = file.read()
    encrypted_data = fernet.encrypt(file_data)
    with open(filepath, "wb") as file:
        file.write(encrypted_data)

def decrypt_file(filepath, key):
    fernet = Fernet(key)
    with open(filepath, "rb") as file:
        encrypted_data = file.read()
    decrypted_data = fernet.decrypt(encrypted_data)
    with open(filepath, "wb") as file:
        file.write(decrypted_data)

def encrypt_string(text, key):
    fernet = Fernet(key)
    encrypted_data = fernet.encrypt(text.encode())
    return encrypted_data.decode()

def decrypt_string(text, key):
    fernet = Fernet(key)
    decrypted_data = fernet.decrypt(text.encode())
    return decrypted_data.decode()

def list_files(directory):
    files_list = []
    for root, _, files in os.walk(directory):
        for file in files:
            files_list.append(os.path.join(root, file))
    return files_list

def main():
    key_file = "encryption_key.key"
    if not os.path.exists(key_file):
        generate_key()

    key = open(key_file, "rb").read()

    while True:
        print("\033[94mSelect a mode:")
        print("1. Encrypt a file")
        print("2. Decrypt a file")
        print("3. Encrypt a message")
        print("4. Decrypt a message")
        print("5. Encrypt a directory")
        print("6. Decrypt a directory")
        print("7. Exit\033[0m")

        mode = int(input("Enter the mode (1/2/3/4/5/6/7): "))

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
            for filepath in list_files(directory):
                encrypt_file(filepath, key)
            print("\033[94mDirectory encrypted successfully.\033[0m")
        elif mode == 6:
            directory = input("Enter the path to the directory you want to decrypt: ")
            for filepath in list_files(directory):
                decrypt_file(filepath, key)
            print("\033[94mDirectory decrypted successfully.\033[0m")
        elif mode == 7:
            print("\033[94mGoodbye!\033[0m")
            break
        else:
            print("\033[94mInvalid mode selection. Please select a valid mode (1/2/3/4/5/6/7).\033[0m")

if __name__ == "__main__":
    main()

