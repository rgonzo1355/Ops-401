import os
import hashlib
import inspect

def hash_file(filename, algorithm='sha1'):
    """This function returns the hash of the file passed into it"""
    if algorithm.lower() == 'sha1':
        hash_func = hashlib.sha1()
    elif algorithm.lower() == 'md5':
        hash_func = hashlib.md5()
    elif algorithm.lower() == 'sha256':
        hash_func = hashlib.sha256()
    else:
        raise ValueError("Unsupported hash algorithm")

    with open(filename, 'rb') as file:
        chunk = 0
        while chunk != b'':
            chunk = file.read(1024)
            hash_func.update(chunk)
    return hash_func.hexdigest()

def search_file(file_name, directory, hash_algorithm='sha1'):
    hits = 0
    files_searched = 0

    if not os.path.isdir(directory):
        print("Error: Invalid directory path.")
        return 0, 0

    print(f"Searching for '{file_name}' in '{directory}'...")

    for root, dirs, files in os.walk(directory):
        for file in files:
            if file == file_name:
                hits += 1
                file_path = os.path.join(root, file)
                print("\033[93mFound:", file_path, "\033[0m")
                if input("Calculate hash of this file? (y/n): ").strip().lower() == 'y':
                    try:
                        print(f"{hash_algorithm.upper()}: {hash_file(file_path, algorithm=hash_algorithm)}")
                    except Exception as e:
                        print(f"Error calculating hash for {file_path}: {e}")
            files_searched += 1
            print_progress(files_searched)

    return hits, files_searched

def print_progress(files_searched):
    print(f"Files searched: {files_searched}", end='\r')

def list_directories():
    current_directory = os.getcwd()
    print("Available directories:")
    for item in os.listdir("/"):
        item_path = os.path.join("/", item)
        if os.path.isdir(item_path):
            if item_path == current_directory:
                print("\033[95m- ", item_path, "(Current Directory)\033[0m")
            else:
                print("\033[95m- ", item_path, "\033[0m")
    print()

def main():
    while True:
        print("\033[32m\nMenu:\033[0m")
        print("1. Search for files")
        print("2. List available directories")
        print("3. Exit")

        choice = input("\033[32mEnter your choice: \033[0m").strip()

        if choice == "1":
            file_name = input("Enter the file name to search for: ").strip()
            directory = input("Enter the directory to search in or type 'list' to see available directories: ").strip()
            hash_algorithm = input("Enter the hash algorithm (sha1/md5/sha256): ").strip()

            if directory.lower() == "list":
                list_directories()
                continue

            if not file_name:
                print("Error: Please provide a file name.")
                continue

            if not directory:
                print("Error: Please provide a directory.")
                continue

            if not os.path.exists(directory):
                print("Error: Directory does not exist.")
                continue

            if hash_algorithm.lower() not in ['sha1', 'md5', 'sha256']:
                print("Error: Unsupported hash algorithm.")
                continue

            search_file(file_name, directory, hash_algorithm)

        elif choice == "2":
            list_directories()

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice. Please enter a number from 1 to 3.")

if __name__ == "__main__":
    main()
