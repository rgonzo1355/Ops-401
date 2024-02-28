#!/usr/bin/env python3
# Rodolfo Gonzalez
# 02-27-2024
# Challenge 37: Web Application Fingerprinting

"""This Python script prompts the user to input a URL, sends a GET request to the provided URL to capture cookies from the response, 
and then prompts the user to select a cookie from the captured list. Subsequently, it sends a new GET request to the URL with the selected cookie. 
It displays the response text, facilitating interaction with websites or 
APIs that require cookie-based authentication or session management. Additionally, it provides clear prompts and error handling for user input and HTTP requests."""

import requests

# Function to capture and display cookies from the response
def capture_cookies(response):
    """Capture and display cookies from the response."""
    print("\033[94mCookies captured from the response:\033[0m")
    if response.cookies:
        for index, cookie in enumerate(response.cookies, 1):
            print(f"\033[92m{index}. Name: {cookie.name}, Value: {cookie.value}\033[0m")
    else:
        print("\033[91mNo cookies found in the response.\033[0m")

# Prompt the user for the URL with an example
url = input("\033[95mEnter the URL (e.g., https://www.example.com): \033[0m")

# Check if the URL has a schema, if not, add 'http://' as default
if not url.startswith('http://') and not url.startswith('https://'):
    url = 'http://' + url

try:
    # Send an initial request to the site to capture the cookies
    response = requests.get(url)
    response.raise_for_status()  # Raise an exception for HTTP errors
except requests.exceptions.RequestException as e:
    print("\033[91mError occurred while making the request:", e, "\033[0m")
    exit()

# Display the captured cookies to the user
capture_cookies(response)

# Check if cookies were found before prompting for index selection
if response.cookies:
    # Prompt the user to select a cookie by index
    cookie_index = input("\033[95mEnter the index of the cookie you want to use: \033[0m")

    try:
        cookie_index = int(cookie_index)
        if cookie_index < 1 or cookie_index > len(response.cookies):
            raise ValueError  # Invalid index
    except ValueError:
        print("\033[91mInvalid input. Please enter a valid index.\033[0m")
        exit()

    # Extract the selected cookie from the response based on the index
    selected_cookie = list(response.cookies)[cookie_index - 1]

    # Now, send the selected cookie back to the site in a new request
    cookies = {selected_cookie.name: selected_cookie.value}  # Ensure passing the value as a string

    try:
        # Make a request to the site with the selected cookie
        response = requests.get(url, cookies=cookies)
        response.raise_for_status()  # Raise an exception for HTTP errors
    except requests.exceptions.RequestException as e:
        print("\033[91mError occurred while making the request:", e, "\033[0m")
        exit()

    # Print the response text with a blue color
    print("\033[94mResponse Text:\033[0m")
    print(response.text)
else:
    print("\033[91mNo cookies found to select. Exiting.\033[0m")
