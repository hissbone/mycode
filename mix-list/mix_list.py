#!/usr/bin/env python3

# create a list
my_list = ['192.168.0.5', 5060, 'UP']

# Print the items of the list with a description
print('The first item in the list (IP): ', my_list[0])
print('The second item in the list (port): ' + str(my_list[1]) )
print('The third item in the list (state): ', my_list[2])

#create a new list
new_list = [ 5060, '80', 55, '10.0.0.1', '10.20.30.1', 'ssh' ]

# print out a messages using all elements of the new list.
print ('When I', new_list[5] + ' into IP address', new_list[3] + ' or', new_list[4] + ' I am unable to ping ports ' + str(new_list[0]) + ',', new_list[1] + ', or ' + str(new_list[2]) +'.')
