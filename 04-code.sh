#!/bin/bash

# Script Name:04-code.sh                
# Class Name:Ops 201
# Author Name:Anthony Wall
# Date of latest revision:02/07/2023
# Purpose:make directories 
# source: chatgbt.com used for explanation of new file dir using new var

# Main 

    mkdir blue1 green2 yellow3 orange4
    directories=("blue1"'green2""yellow3""orange4")

    for dir in "${directories}
    do 
    touch "${dir}/file.txt"



# End  