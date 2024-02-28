#!/usr/bin/env python3
# Rodolfo Gonzalez
# 02-28-2024
# Challenge 38: XSS Vulnerability Detection with Python

"""This script utilizes ANSI escape codes to display colored output in the terminal. It defines several colors for different types of messages. 
Then, it defines a function check_xss_vulnerability(URL) to check for XSS vulnerabilities in the given URL. 
It sends a GET request to the target URL with a payload containing a script tag to detect if the payload is reflected in the response. 
If the payload is found in the answer, it indicates a potential XSS vulnerability. If an error occurs during the request, it prints a warning message."""

import requests

# ANSI escape codes for colors
COLOR_RED = "\033[91m"
COLOR_GREEN = "\033[92m"
COLOR_YELLOW = "\033[93m"
COLOR_CYAN = "\033[96m"
COLOR_PURPLE = "\033[95m"
COLOR_RESET = "\033[0m"

def check_xss_vulnerability(url):
    try:
        # Define payload for testing XSS
        payload = "<script>alert('XSS Vulnerability Detected!');</script>"
        
        # Send a GET request to the target URL with the payload
        response = requests.get(url + payload)
        
        # Check if the payload is reflected in the response
        if payload in response.text:
            print(COLOR_RED + "[+] XSS Vulnerability Detected in:" + COLOR_CYAN, url)
        else:
            print(COLOR_GREEN + "[-] No XSS Vulnerability Detected in:" + COLOR_CYAN, url)
    except requests.RequestException as e:
        print(COLOR_YELLOW + "[!] Error occurred while connecting to the URL:" + COLOR_RESET, str(e))

if __name__ == "__main__":
    while True:
        # Ask the user to input the target URL
        target_url = input(COLOR_PURPLE + "Enter the target URL to check for XSS vulnerability: Ex: https://xss-game.appspot.com/level1/frame \n" + COLOR_RESET)
        
        check_xss_vulnerability(target_url)
        
        # Ask the user if they want to perform another search
        another_search = input("Do you want to perform another search? (y/n): ").lower()
        if another_search != 'y':
            break
