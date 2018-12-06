#!/usr/bin/env python3

#create file object in read mode
configfile = open('vlanconfig.cfg', 'r')

#assign a string variable
configblog = configfile.read()

#display the file to the screen = .read()
print(configblog)

#break configblog across line boundaries (strip out newline)
configlist = configblog.splitlines()

#display list with no newlines
print(configlist)

#always close your file
configfile.close()
