#!/usr/bin/env python3

# Prompt the user for a number
num = int(input('Enter a number: '))
f = 1  # initialize the factor to 1
for i in range(1, num + 1):  # loop through a range of numbers
    f = f * i               # perform the calculation
    print(str(num) + '! = ', f)

