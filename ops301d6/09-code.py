#!/user/bin/env python3

# Script Name:                  03-code.sh                
# Class Name:                   Ops 301
# Author Name:                  Anthony Wall
# Date of latest revision:      03/23/2023
# Creates: Create if statements using these logical conditionals below. Each statement should print information to the screen depending on if the condition is met.
a = 10
b = 5

# Equals
if a == b:
    print("a equals b")

# Not Equals
if a != b:
    print("a does not equal b")

# Less than
if a < b:
    print("a is less than b")

# Less than or equal to
if a <= b:
    print("a is less than or equal to b")

# Greater than
if a > b:
    print("a is greater than b")

# Greater than or equal to
if a >= b:
    print("a is greater than or equal to b")

# If-elif statement
if a == b:
    print("a equals b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# If-elif-else statement
if a == b:
    print("a equals b")
elif a < b:
    print("a is less than b")
else:
    print("a is greater than b")

# And statement
if a < 20 and b > 2:
    print("Both conditions are true")

# Or statement
if a < 5 or b > 10:
    print("At least one condition is true")

# Nested if statement
if a > 5:
    print("a is greater than 5")
    if b < 10:
        print("b is less than 10")

# If statement with pass
if a == b:
    pass
else:
    print("a does not equal b")

#sorce: leran linux tv chatgbt.com