#!/user/bin/env python

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/20/2023
# Purpose: Creats a script to perfrom a python script.

import os

# Execute bash command 'whoami' and store output in variable 'user'
user = os.popen('whoami').read().strip()

# Execute bash command 'ip a' and store output in variable 'ip_addresses'
ip_addresses = os.popen('ip a').read()

# Execute bash command 'lshw -short' and store output in variable 'hardware_info'
hardware_info = os.popen('lshw -short').read()

# Print the variables containing the results of the bash commands
print("Current user: ", user)
print("IP addresses: ", ip_addresses)
print("Hardware information: ", hardware_info)


# stretch goals 

import subprocess

# Execute bash command 'whoami' and store output in variable 'user'
user = subprocess.check_output(['whoami']).decode('utf-8').strip()

# Execute bash command 'ip a' and store output in variable 'ip_addresses'
ip_addresses = subprocess.check_output(['ip', 'a']).decode('utf-8')

# Execute bash command 'lshw -short' and store output in variable 'hardware_info'
hardware_info = subprocess.check_output(['lshw', '-short']).decode('utf-8')

# Print the variables containing the results of the bash commands
print("Current user: ", user)
print("IP addresses: ", ip_addresses)
print("Hardware information: ", hardware_info)

# Source: chatgbt.com

