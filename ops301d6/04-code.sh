#!/bin/bash

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/16/2023
# Purpose: Create a bash script to perform simple commands 

while true
do
    echo "Please select an option:"
    echo "1. Hello world"
    echo "2. Ping self"
    echo "3. IP info"
    echo "4. Exit"

    read choice

    case $choice in
        1) echo "Hello world!" ;;
        2) ping 127.0.0.1 ;;
        3) ifconfig ;;
        4) exit ;;
        *) echo "Invalid option. Please try again." ;;
    esac
done

# source // chatgbt.com