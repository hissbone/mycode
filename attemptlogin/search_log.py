#!/usr/bin/env python3

loginfail = 0 # initialize the counter to 0

keystone_file = open('/home/student/mycode/attemptlogin/keystone.common.wsgi', 'r') # open a file for reading

keystone_file_lines = keystone_file.readlines() # read each line of the file into a string

for line in range(len(keystone_file_lines)):   # loop through each line
    if 'Authorization failed' in keystone_file_lines[line]: # test to see if a string was found in the lines
        loginfail += 1                                # increment the counter
        #print(keystone_file_lines[line].split('from ')) ...this was a test to see if the split method would work
        ip_list = (keystone_file_lines[line].split('from '))  # assign the list created to ip_list
        print('Source IP for failed login: ', ip_list[1], end='')  # print the second element of the list which is the IP address
print('The number of failed login attempts is: ' + str(loginfail))  # print a message with the number of failed logins
