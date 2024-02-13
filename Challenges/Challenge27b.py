#!/usr/bin/python3

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

# Create file handler object
log_file = 'my_logs.log'
handler_file = RotatingFileHandler(log_file, maxBytes=10000, backupCount=3)

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
logger.addHandler(handler_file)
logger.addHandler(handler_console)

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
