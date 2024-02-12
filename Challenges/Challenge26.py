#!/usr/bin/python3
# Import libraries
import logging
import os

# Create the log object
log = logging.getLogger("my_logger")

log.info("Hello, You!")

# Define the function
def do_something():
    log.debug("Doing something!")

# Call our function
do_something()
