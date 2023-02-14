#!/bin/bash

# Script: Class_6                    
# Author: Anthony Wall                        
# Date of latest revision: 02/13/2023     
# Purpose: This scrip detects is a file or directory exsist and if not creadit it.

# Main 

import os

path = "C:\Users\Public\Logi\registry.json"

if not os.path.exists(path):
    os.makedirs(path)
    print("Created:", path)
else:
    print(path, "already exists")

#End
