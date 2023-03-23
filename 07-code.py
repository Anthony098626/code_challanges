#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/21/2023
# Creates a Python script that generates all directories, sub-directories and files for a user-provided directory path. 

import os

def generate_file_tree(path):
    for root, dirs, files in os.walk(path):
        level = root.replace(path, '').count(os.sep)
        indent = ' ' * 4 * level
        print('{}{}/'.format(indent, os.path.basename(root)))
        sub_indent = ' ' * 4 * (level + 1)
        for file in files:
            print('{}{}'.format(sub_indent, file))

if __name__ == '__main__':
    path = input("Enter directory path: ")
    generate_file_tree(path)

#stretch goals

import os
import subprocess

# Function to create directory with subdirectories
def create_directory():
    # Take user input for directory name
    dirname = input("Enter a directory name: ")
    
    # Create the directory
    os.makedirs(dirname)

    # Create subdirectories
    for i in range(1, 4):
        os.makedirs(os.path.join(dirname, f"{dirname}_0{i}"))

# Call create_directory function
create_directory()

# Execute bash commands using subprocess module
whoami = subprocess.check_output(["whoami"]).decode().strip()
ip_a = subprocess.check_output(["ip", "a"]).decode().strip()
lshw_short = subprocess.check_output(["lshw", "-short"]).decode().strip()

# Print the results
print(f"Current user: {whoami}")
print(f"IP configuration: \n{ip_a}")
print(f"Hardware summary: \n{lshw_short}")

# Save output to a text file
with open("output.txt", "w") as f:
    f.write(f"Current user: {whoami}\n")
    f.write(f"IP configuration: \n{ip_a}\n")
    f.write(f"Hardware summary: \n{lshw_short}\n")

# Open text file with Libre Office Writer
subprocess.call(["libreoffice", "--writer", "output.txt"])


# source: chatgbe.com