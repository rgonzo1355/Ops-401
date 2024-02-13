#!/usr/bin/python3
# Rodolfo Gonzalez
# 02-13-2024
# Challenge 27          Event Logging Tool 2 of 3.

"""
This Python script sets up a logging system that logs messages to both a file and the console. 
It uses a RotatingFileHandler to ensure that log files don't grow too large, rotating them when they reach a certain size limit while keeping a specified number of backup files. 
The script also includes a menu function that allows users to select different logging levels interactively."""
# resources: https://chat.openai.com/share/745d9875-c97f-4648-a03c-ddc464fa2bad

# Import Libraries
import logging
import time
import os
from logging.handlers import RotatingFileHandler
from logging import StreamHandler
import colorlog

# Create logger object and name it my_logger
logger = logging.getLogger('my_logger')
logger.setLevel(logging.DEBUG)  # Set default logging level to DEBUG

# Define log file name
log_file = 'my_logs.log'

# Create file handler object with log rotation capabilities
# RotatingFileHandler rotates log files when they reach a certain size (maxBytes),
# and keeps a certain number of backup log files (backupCount)
handler_file = RotatingFileHandler(log_file, maxBytes=10_000_000, backupCount=3)  # 10MB size limit, keeping 3 backup files

# Create console handler object
handler_console = StreamHandler()

# Set logging format
formatter = colorlog.ColoredFormatter(
    '%(log_color)s%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    log_colors={
        'DEBUG': 'cyan',
        'INFO': 'green',
        'WARNING': 'yellow',
        'ERROR': 'red',
        'CRITICAL': 'red,bg_white',
    },
)
handler_file.setFormatter(formatter)
handler_console.setFormatter(formatter)

# Add handlers to logger
logger.addHandler(handler_file)  # Add file handler for logging to file
logger.addHandler(handler_console)  # Add console handler for logging to console

# Menu function
def prompt_menu():
    while True:
        print("\033[95mSelect logging level:\033[0m")
        print("1. DEBUG")
        print("2. INFO")
        print("3. WARNING")
        print("4. ERROR")
        print("5. CRITICAL")
        print("6. Exit")
        choice = input("\033[95mEnter your choice (1-6): \033[0m")
        if choice == '1':
            logger.setLevel(logging.DEBUG)
        elif choice == '2':
            logger.setLevel(logging.INFO)
        elif choice == '3':
            logger.setLevel(logging.WARNING)
        elif choice == '4':
            logger.setLevel(logging.ERROR)
        elif choice == '5':
            logger.setLevel(logging.CRITICAL)
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")

        # For loop
        for i in range(3):
            try:
                logmsg = "Howdy!"
                logmsg += str(i)
                logger.debug(logmsg)
                logger.info(logmsg)
                logger.warning(logmsg)
                logger.error(logmsg)
                logger.critical(logmsg)
                print("Logging Howdy! number", i)
                os.system("ls -al")
                time.sleep(0.1)
            except Exception as e:
                print("Error:", e)

# Prompt user for logging level
prompt_menu()
