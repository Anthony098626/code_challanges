#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/28/2023
# Creates:creates a python script that performs basic commands 

import requests

# Prompt the user to enter a destination URL
url = input("Enter the destination URL: ")

# Prompt the user to select a HTTP method
http_method = input("Select a HTTP method (GET, POST, PUT, DELETE, HEAD, PATCH, OPTIONS): ")

# Print the entire request to the screen and ask for confirmation
print(f"\nSending {http_method} request to {url}")
confirmation = input("Confirm? (y/n): ")

if confirmation.lower() != "y":
    print("Request cancelled.")
    exit()

# Set authentication credentials
username = input("Enter your GitHub username: ")
token = input("Enter your GitHub access token: ")
auth = (username, token)

# Set timeouts for the request
timeout = 10

try:
    # Perform the HTTP request with authentication and timeouts
    response = requests.request(http_method, url, auth=auth, timeout=timeout)

    # Translate response codes into plain terms and print to the screen
    if response.status_code == 200:
        print("Request successful!")
    elif response.status_code == 404:
        print("Site not found")
    elif response.status_code == 500:
        print("Internal server error")
    else:
        print(f"Request failed with status code: {response.status_code}")

    # Print response header information to the screen
    print("\nResponse headers:")
    for header, value in response.headers.items():
        print(f"{header}: {value}")

except requests.exceptions.Timeout:
    # Handle timeout error
    print("Request timed out. Please try again later.")

except requests.exceptions.RequestException as e:
    # Handle all other types of exceptions
    print(f"An error occurred: {e}")

# source https://chat.openai.com/chat