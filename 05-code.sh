#!/bin/bash

# Script: Class_5                      
# Author: Anthony Wall                        
# Date of latest revision: 02/10/2023     
# Purpose: This scrip displays a running process, asks user for PID, then kills with PID 

# source https://chat.openai.com/chat 

# Main 
import os

print("List of running processes:")
processes = os.popen("ps -e").read()
print(processes)

pid = int(input("Enter PID of the process to be killed: "))

os.system(f"kill {pid}")
print(f"Process with PID {pid} has been killed.")
# End 