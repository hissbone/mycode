#!/usr/bin/env python3

####################explore read##################

#create file object in read mode
configfile = open('vlanconfig.cfg', 'r')

# display file to the screen - .read()
print(configfile.read())

#close file
configfile.close()

######explore readlines#################
#re-create file object in read mode
configfile = open('vlanconfig.cfg', 'r')

#make a list fo file lines - .readlines()
configlist = configfile.readlines()
print(configlist)

#Iterate through configlist
for x in configlist:
    print(x, end='')

#Always close your file
configfile.close()
