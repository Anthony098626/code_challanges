#!/bin/bash

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/17/2023
# Purpose: Creats a script to perfrom bash instructions. 

# Print file size of log files before compression
echo "File sizes before compression:"
ls -lh /var/log/syslog
ls -lh /var/log/wtmp

# Create backup directory
mkdir -p /var/log/backups

# Compress log files to backup directory with timestamped file name
timestamp=$(date +"%Y%m%d%H%M%S")
zip /var/log/backups/syslog-$timestamp.zip /var/log/syslog
zip /var/log/backups/wtmp-$timestamp.zip /var/log/wtmp

# Clear contents of log files
echo "" > /var/log/syslog
echo "" > /var/log/wtmp

# Print file size of compressed files
echo "File sizes after compression:"
ls -lh /var/log/backups/syslog-$timestamp.zip
ls -lh /var/log/backups/wtmp-$timestamp.zip

# Compare size of compressed files to original log files
echo "Comparison of file sizes:"
du -h /var/log/syslog
du -h /var/log/wtmp
du -h /var/log/backups/syslog-$timestamp.zip
du -h /var/log/backups/wtmp-$timestamp.zip

# source 
* https://chat.openai.com/chat 