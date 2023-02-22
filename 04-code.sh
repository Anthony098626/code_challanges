#!/bin/bash

# Script Name:04-code.sh                
# Class Name:Ops 201
# Author Name:Anthony Wall
# Date of latest revision:02/07/2023
# Purpose:make directories 
# source: chatgbt.com used for explanation of new file dir using new var

# Main 

dir_create() {
    mkdir blue green yellow orange
    dir_array=("./blue/" "./green/" "./yellow/" "./orange/")   
}

file_create() {
    touch "${dir_array[0]}file0.txt"
    touch "${dir_array[1]}file1.txt"
    touch "${dir_array[2]}file2.txt"
    touch "${dir_array[3]}file3.txt"
}
   
dir_create

file_create
