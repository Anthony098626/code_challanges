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
# Ask the user for an email address and password to use for sending notifications.
email = input("anthony098626@gmail.com")
password = input("4NuUn!MGk]xjD3c9aEHK")
# Send an email to the administrator if a host status changes (from “up” to “down” or “down” to “up”).
import smtplib

def send_email_notification(message):
    sender_email = "anthony098626.lab@gmail.com"
    sender_password = "4NuUn!MGk]xjD3cpaEHK"
    recipient_email = "anthony098626@gmail.com"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login(sender_email, sender_password)

        subject = "Host status changed!"
        body = message

        email_message = f"Subject: {subject}\n{body}"
        smtp.sendmail(sender_email, recipient_email, email_message.encode('utf-8'))

host_status = "down" # this variable would hold the actual status of the host (up or down)
host_status_changed = True # set to True if host_status has changed, else False

# this would check if the host status had changed at any point
if host_status_changed:
    message = f"Host status changed to {host_status}!"
    send_email_notification(message)

# Clearly indicate in the message which host status changed, the status before and after, and a timestamp of the event.
import smtplib
from datetime import datetime

def send_email_notification(message):
    sender_email = "anthony098626@gmail.com" # fixed typo
    sender_password = "4NuUn!MGk]xjD3c9aEHK"
    recipient_email = "anthony098626@gmail.com"

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        try:
            smtp.login(sender_email, sender_password)
        except smtplib.SMTPAuthenticationError:
            print("Could not login to email server")

        subject = "Host status changed!"
        body = message

        email_message = f"Subject: {subject}\n{body}\n" # ended with single newline
        smtp.sendmail(sender_email, recipient_email, email_message.encode('utf-8'))

previous_host_status = "up"
current_host_status = "down"
timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

if previous_host_status != current_host_status:
    message = f"Host status has changed from {previous_host_status} to {current_host_status} at {timestamp}."
    
    send_email_notification(message)

# source: openai.com