# Rodolfo Gonzalez
# 01-10-2024
# Uptime Sensor Tool Part 2 of 2

'''Finish writing an uptime sensor tool that checks systems are responding by adding a feature that notifies you of interesting status changes.
The script must:

-Ask the user for an email address and password to use for sending notifications.
-Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
-Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.

Resources: 
https://g.co/bard/share/dc8ba53a59fc 
https://towardsdatascience.com/how-to-easily-automate-emails-with-python-8b476045c151
'''

import os
import subprocess
import time

def ping(host):
    
    # Function to send an ICMP ping packet to the specified host.
    
    try:
        # Use 'ping' command based on the OS (Windows or non-Windows)
        response = subprocess.check_output(['ping', '-n', '1', host]) if os.name == 'nt' else subprocess.check_output(['ping', '-c', '1', host])
        return True  # If ping succeeds, return True
    except subprocess.CalledProcessError:
        return False  # If ping fails, return False

def main():
    host = "8.8.8.8"  # Replace with the IP address you want to ping
    interval = 2  # Interval in seconds between pings

    while True:
        timestamp = time.strftime('%Y-%m-%d %H:%M:%S.%f')  # Get current timestamp
        is_alive = ping(host)  # Check if host is reachable
        status = "Network Active" if is_alive else "Network Down"  # Set status based on reachability
        
        # Print timestamp, status, and destination IP
        print(f"{timestamp} {status} to {host}")

        time.sleep(interval)  # Wait for the specified interval before the next ping

if __name__ == "__main__":
    main()  # Start the main function when the script is executed
