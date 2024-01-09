# Rodolfo Gonzalez
# 01-09-2024

# Uptime Sensor Tool Part 1 of 2


"""# Get input from the user
input1 = input("Enter the first piece of input: ")
input2 = input("Enter the second piece of input: ")

# Get the number of times to print
num_times = int(input("Enter the number of times to print: "))

# Print the inputs the specified number of times
for i in range(num_times):
    print(f"{input1} {input2}") """

import os
import subprocess
import time

def ping(host):
    """
    Function to send an ICMP ping packet to the specified host.
    """
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

# Resources: https://g.co/bard/share/dc8ba53a59fc 
