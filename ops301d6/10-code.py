#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/23/2023
# Creates: a new txt.file / add's 3 lines of context / prints line 1 to screen / then delets said file

# New txt.file
with open("Anthony's_file.txt", "w") as file:
    # Write three lines to the file
    file.write("God\n")
    file.write("Bless\n")
    file.write("America\n")

# Open the file in read mode and print the first line to the console
with open("Anthony's_file.txt", "r") as file:
    print(file.readline())

# Delete the file
import os
os.remove("my_file.txt")

# Sources: https://chat.openai.com/chat 

