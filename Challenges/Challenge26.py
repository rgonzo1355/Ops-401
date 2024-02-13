#!/usr/bin/env python3

# Rodolfo Gonzalez
# February 12 2024
# Challenge 27          Event Logging Tool 1 of 3.
"""The code implements a Python script that manipulates a list of fruits, performing various operations such as appending, 
inserting, removing, and sorting elements. It incorporates logging capabilities to record these operations, 
categorizing log messages by severity with corresponding colors, and outputs them to a log file for monitoring and analysis. 
The script enhances readability and user engagement by infusing a playful theme centered around fruits, making the logging process informative and enjoyable."""
# Contribuitors: Juan Cano



import logging

# Define ANSI escape codes for colors
class Colors:
    RESET = "\033[0m"
    RED = "\033[31m"
    GREEN = "\033[32m"
    YELLOW = "\033[33m"
    BLUE = "\033[34m"
    PURPLE = "\033[35m"
    CYAN = "\033[36m"
    WHITE = "\033[37m"
    BOLD = "\033[1m"

# Configure logging settings
logging.basicConfig(filename='collections_tool.log', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

def color_log_message(message, color):
    return f"{color}{message}{Colors.RESET}"

def print_and_log(message, color=None):
    if color:
        message = color_log_message(message, color)
    print(message)
    logging.info(message)

def main():
    # Step 1: Assign a list of ten string elements to a variable
    my_list = ["Apple", "Banana", "Cherry", "Durian", "Elderberry", "Fig", "Grape", "Honeydew", "Kiwi", "Lemon"]

    try:
        # Step 2: Print the fourth element of the list
        print_and_log("Fourth element: {}".format(my_list[3]), Colors.GREEN)

        # Step 3: Print the sixth through tenth elements of the list
        print_and_log("Sixth through tenth elements: {}".format(my_list[5:]), Colors.GREEN)

        # Step 4: Change the value of the seventh element to "SNCO"
        my_list[6] = "Mango"
        print_and_log("Updated list: {}".format(my_list), Colors.GREEN)

        # Stretch Goals:

        # Use the append() method to add a new element to the list
        my_list.append("Orange")
        print_and_log("List after appending 'Orange': {}".format(my_list), Colors.GREEN)

        # Use the clear() method to empty the list
        my_list.clear()
        print_and_log("List after clearing: {}".format(my_list), Colors.GREEN)

        # Create a copy of the original list using the copy() method
        original_list = ["Apple", "Banana", "Cherry"]
        copied_list = original_list.copy()
        print_and_log("Original list: {}".format(original_list), Colors.GREEN)
        print_and_log("Copied list: {}".format(copied_list), Colors.GREEN)

        # Use the count() method to count the occurrences of a specific element
        count_Banana = original_list.count("Banana")
        print_and_log("Count of 'Banana': {}".format(count_Banana), Colors.GREEN)

        # Use the extend() method to extend the list with another list
        extension_list = ["Grapefruit", "Pineapple"]
        original_list.extend(extension_list)

        # Use the index() method to find the index of a specific element
        try:
            index_Mango = original_list.index("Mango")
            print_and_log("Index of 'Mango': {}".format(index_Mango), Colors.GREEN)
        except ValueError:
            print_and_log("'Mango' is not in the list", Colors.YELLOW)
            logging.warning("'Mango' is not in the list")

        # Use the insert() method to insert an element at a specific index
        original_list.insert(1, "Papaya")
        print_and_log("List after inserting 'Papaya' at index 1: {}".format(original_list), Colors.GREEN)

        # Use the pop() method to remove and return an element at a specific index
        removed_element = original_list.pop(3)
        print_and_log("Removed element at index 3: {}".format(removed_element), Colors.GREEN)
        print_and_log("List after pop: {}".format(original_list), Colors.GREEN)

        # Use the remove() method to remove a specific element
        try:
            original_list.remove("Mango")
            print_and_log("List after removing 'Mango': {}".format(original_list), Colors.GREEN)
        except ValueError:
            print_and_log("Cannot remove 'Mango' from the list: 'Mango' is not in the list", Colors.YELLOW)
            logging.warning("'Mango' is not in the list")

        # Use the reverse() method to reverse the order of elements in the list
        original_list.reverse()
        print_and_log("Reversed list: {}".format(original_list), Colors.GREEN)

        # Use the sort() method to sort the elements in the list
        original_list.sort()
        print_and_log("Sorted list: {}".format(original_list), Colors.GREEN)

        # Create a tuple
        my_tuple = ("Apple", "Banana", "Cherry")

        # Create a set
        my_set = {"Apple", "Banana", "Cherry"}

        # Create a dictionary
        my_dict = {"Fruits1": "Apple", "Fruits2": "Banana", "Fruits3": "Cherry"}

        # Print the created tuple, set, and dictionary
        print_and_log("Tuple: {}".format(my_tuple), Colors.GREEN)
        print_and_log("Set: {}".format(my_set), Colors.GREEN)
        print_and_log("Dictionary: {}".format(my_dict), Colors.GREEN)
    except Exception as e:
        logging.error("An error occurred: {}".format(str(e)), Colors.RED)

if __name__ == "__main__":
    main()
