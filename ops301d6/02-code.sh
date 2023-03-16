#!/bin/bash

# Script Name:                  02-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/14/2023
# Purpose: creat a script that prints prints date and time. 


# Get the current date and time
now=$(date +"%Y-%m-%d_%H-%M-%S")

# Copy the syslog file to the current working directory and append the date and time to the filename
cp /var/log/syslog ./syslog_$now

#End

# help from chat gbt