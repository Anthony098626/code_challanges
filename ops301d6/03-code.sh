#!/bin/bash

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/15/2023
# Purpose: Create a bash script to perform commands.

# Prompt user for directory path
read -p "Enter directory path: " dir_path

# Prompt user for permission number
read -p "Enter permission number: " permission

# Navigate to directory and change permissions of all files
cd $dir_path
echo "Changing permissions of all files in $dir_path to $permission"
chmod -R $permission *

# Output directory contents and permissions
echo "Directory contents and permissions:"
ls -l

# Output changes to a log file
echo "Changes made:" > change_log.txt
ls -l >> change_log.txt
echo "Permissions changed to $permission" >> change_log.txt

# Output each file changed one by one with a slight delay
echo "Changing each file one by one..."
for file in *
do
  if [ -f $file ]; then
    echo "Changing permission of $file to $permission"
    chmod $permission $file
    sleep 0.5s
  fi
done
