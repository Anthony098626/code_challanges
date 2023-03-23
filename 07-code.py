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


# source: chatgbe.com