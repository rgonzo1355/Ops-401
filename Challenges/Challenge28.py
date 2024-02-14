

#!/usr/bin/env python3
# Script Name:                 Ops Challenge: Ops Challenge: Event Logging Tool Part 3 of 3
# Author:                      Rodolfo Gonzalez
# Date of latest revision:     02/14/2024

# Purpose:                  StreamHandler and FileHandler 
# Purpose:                  Incorporating logging capabilities using handlers for both timed rotating file logs and regular file logs, alon with logging to the terminal.
# Purpose 2:                Demonstrate the manipulation of lists and the use of various list methods, including basic operations and involving tuples, sets, and dictionaries.                    
# Resource:                 https://chat.openai.com/share/35f7747d-4bc3-4c85-9845-612d7913c439
                            # https://chat.openai.com/share/bf7fba6c-dbf3-4d0a-b8fe-757d3aa5fda1 
# Team member:              Juan Cano


import logging
import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')


import logging
import os
import time
from logging.handlers import TimedRotatingFileHandler
from colorlog import ColoredFormatter

# Create logging settings
logger = logging.getLogger('myTimedLogger')
logger.setLevel(logging.DEBUG)

# Create and configure handler for timed rotating file logs
# This will rotate the log file every day, keeping 7 days of backup logs
handler = TimedRotatingFileHandler('timed_collections_tool.log', when="D", interval=1, backupCount=7)
handler.setLevel(logging.DEBUG)
handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(handler)

# Create and configure FileHandler for logging to a file
file_handler = logging.FileHandler('collections_tool.log')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logger.addHandler(file_handler)

# Create and configure StreamHandler for logging to terminal with color
stream_handler = logging.StreamHandler()
stream_handler.setLevel(logging.INFO)  # Adjust level as needed
color_formatter = ColoredFormatter('%(log_color)s%(asctime)s - %(levelname)s - %(message)s')
stream_handler.setFormatter(color_formatter)
logger.addHandler(stream_handler)

for i in range(5):
    logmsg = "Aye Aye Sir " + str(i)
    logger.warning(logmsg)
    print("Logging Aye Aye Sir", i)
    os.system("ls -al")
    time.sleep(0.1)

# Assign a list of ten string elements to a variable
my_list = ["Pvt", "PFC", "LCpl", "Cpl", "Sgt", "SSgt", "GySgt", "MGySgt", "1stSgt", "SgtMaj"]

# Step 2: Print the fourth element of the list
print("Fourth element:", my_list[3])
logger.info('Printed the fourth element of the list')

# Step 3: Print the sixth through tenth elements of the list
print("Sixth through tenth elements:", my_list[5:])
logger.info('Printed the sixth through tenth elements of the list')

# Step 4: Change the value of the seventh element to "SNCO"
my_list[6] = "SNCO"
print("Updated list:", my_list)
logger.info('Updated the list by changing the value of the seventh element')

# Stretch Goals:

# Use the append() method to add a new element to the list
my_list.append("Marine")
print("List after appending 'Marine':", my_list)
logger.info('Appended "Marine" to the list')

# Use the clear() method to empty the list
my_list.clear()
print("List after clearing:", my_list)
logger.info('Cleared the list')

# Create a copy of the original list using the copy() method
original_list = ["Pvt", "Pfc", "LCpl"]
copied_list = original_list.copy()
print("Original list:", original_list)
print("Copied list:", copied_list)
logger.info('Created a copy of the original list')

# Use the count() method to count the occurrences of a specific element
count_Pfc = original_list.count("Pfc")
print("Count of 'Pfc':", count_Pfc)
logger.info('Counted occurrences of "Pfc" in the list')

# Use the extend() method to extend the list with another list
extension_list = ["NCO", "SNCO"]
original_list.extend(extension_list)
print("List after extending:", original_list)

# Use the index() method to find the index of a specific element
try:
    index_SSgt = original_list.index("SSgt")
    print("Index of 'SSgt':", index_SSgt)
except ValueError:
    print("'SSgt' is not in the list")
    logger.warning("'SSgt' is not in the list")

# Use the insert() method to insert an element at a specific index
original_list.insert(1, "GySgt")
print("List after inserting 'GySgt' at index 1:", original_list)
logger.info('Inserted "GySgt" at index 1 in the list')

# Use the pop() method to remove and return an element at a specific index
removed_element = original_list.pop(3)
print("Removed element at index 3:", removed_element)
print("List after pop:", original_list)
logger.info('Removed an element at index 3 from the list')

























































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































































