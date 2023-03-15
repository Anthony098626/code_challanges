#!/bin/bash

# Script: Class_5                      
# Author: Anthony Wall                        
# Date of latest revision: 02/10/2023     
# Purpose: This scrip displays a running process, asks user for PID, then kills with PID 

# source https://chat.openai.com/chat 

# Main 

while true
do
    ps -aux
    echo "Run as Admin for full functionality"
    echo "Enter PID of Process you would like to kill:"
    read kill_PID

    kill $kill_PID
done

# End 