#!/user/bin/python3
import os
import sys
import datetime
import platform
import subprocess
import time

# Function to ping an IP address
def ping(host):
    if platform.system().lower() == "windows":
        ping_str = "-n 1"
    else:
        ping_str = "-c 1"
    # Use subprocess to run the ping command and capture the output
    return subprocess.call(["ping", ping_str, host], stdout=subprocess.PIPE) == 0

# IP address to ping
ip_address = "8.8.8.8"
# Status variable to hold whether the ping was successful or not
status = ""

while True:
    # Get the current time
    current_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    # Ping the IP address
    if ping(ip_address):
        # If the ping was successful, set the status variable to "Success"
        status = "Success"
    else:
        # If the ping failed, set the status variable to "Failed"
        status = "Failed"
    # Print the timestamp, IP address tested, and status variable
    print("{} - {} - {}".format(current_time, ip_address, status))
    # Wait for 2 seconds before pinging again
    time.sleep(2)