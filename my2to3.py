#!/usr/bin/env python3

thisround = 0  # counter initiated to 0
while(True):  #   sets up an infinite loop
    print('What is the IPv4 address used to broadcast on a local network? ')
    answer = input()   # string answer collected from user
    thisround = thisround + 1  # increment the counter
    if (answer == '255.255.255.255'): # test to see if correct answer given
        print('Correct!')
        break              # break statement escapes the while loop
    elif (thisround == 3):  # test to see if counter has reached limit
        print('Sorry, the answer was 255.255.255.255.')
        break              # break statement escapes the while loop
    else:                  # if answer was incorrect and counter not at limit
        print('Sorry.  Try again!')


