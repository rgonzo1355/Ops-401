#!/usr/bin/python3
# Rodolfo Gonzalez
# 02-19-2024
# Challenge 32 Singnature-based malware Detection Part 1 of 3

"""This code serves as a utility for searching specific files within a given directory and its subdirectories, 
allowing the user to list all available directories"""

import os

# Function to search for a file in a directory
def search_file(file_name, directory):
    hits = 0  # Initialize the variable to count the number of hits (matching files)
    files_searched = 0  # Initialize the variable to count the total number of files searched

    # Check if the provided directory path is valid
    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return 0, 0  # Return 0 hits and 0 files searched if the directory is invalid

    print(f"Searching for '{file_name}' in '{directory}'...")  # Print the search message

    # Recursively search for files in the specified directory and its subdirectories
    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:  # If the file matches the search criteria
                hits += 1  # Increment the hit count
                file_path = os.path.join(root, file)  # Get the full path of the file
                # Print the full path of the found file in yellow
                print("\033[93mFound:", file_path, "\033[0m")  # This will display "Found: [file_path]" in yellow


            files_searched += 1  # Increment the total files searched count
            print_progress(files_searched)  # Print the progress of the search

    return hits, files_searched  # Return the total hits and files searched

# Function to print the progress of the search
def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')  # Print the current progress without newline

# Function to list available directories with modifications for vertical listing and purple color
def list_directories():
    current_directory = os.getcwd()  # Get the current working directory
    print("Available directories:")  # Print the heading for the available directories
    for item in os.listdir("/"):  # Iterate through items in the root directory
        item_path = os.path.join("/", item)  # Get the full path of the item
        if os.path.isdir(item_path):  # If the item is a directory
            if item_path == current_directory:  # If the item is the current working directory
                # Print the current directory in purple color with a label (using  color code \033[92m)
                print("\033[95m- ", item_path, "(Current Directory)\033[0m")
            else:
                # Print other directories in purple color (using light purple color code \033[95m)
                print("\033[95m- ", item_path, "\033[0m")
    print()  # Add a newline character to separate the list from the menu

# Function to search for files
def search_files():
    file_name = input("Enter the file name to search for: ").strip()  # Get the file name to search for
    directory = input("Enter the directory to search in or type 'list' to see available directories: ").strip()  # Get the directory to search in

    if directory.lower() == "list":  # If the user wants to list available directories
        list_directories()  # Call the function to list directories
        return  # Exit the function

    if not file_name:  # If the file name is not provided
        print("Error: Please provide a file name.")
        return

    if not directory:  # If the directory is not provided
        print("Error: Please provide a directory.")
        return

    if not os.path.exists(directory):  # If the directory does not exist
        print("Error: Directory does not exist.")
        return

    hits, files_searched = search_file(file_name, directory)  # Search for files in the specified directory

    if hits == 0 and files_searched == 0:  # If no files were searched due to a directory error
        print("\nNo files searched due to directory error.")
    else:
        print("\nTotal files searched:", files_searched)  # Print the total number of files searched
        # Print the total number of hits (matching files) in yellow
        print(f"\033[93mTotal hits found: {hits}\033[0m")


# Main function to run the program
def main():
    while True:
        print("\033[32m\nMenu:\033[0m")  # Print the main menu in green color
        print("1. Search for files")
        print("2. List available directories")
        print("3. Exit")

        choice = input("\033[32mEnter your choice: \033[0m").strip()  # Get the user's choice in green color

        if choice == "1":  # If the user chooses to search for files
            search_files()  # Call the function to search for files
        elif choice == "2":  # If the user chooses to list available directories
            list_directories()  # Call the function to list directories
        elif choice == "3":  # If the user chooses to exit
            print("Exiting...")  # Print the exit message
            break  # Exit the loop and end the program
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")  # If the user enters an invalid choice

# Entry point of the program
if __name__ == "__main__":
    main()  # Call the main function when the script is executed
