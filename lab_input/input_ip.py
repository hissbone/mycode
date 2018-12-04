#!/usr/bin/env python3
# Written By: Stephen Christensen
# Collect IP address information from a user and display it back to them.

# Prompt user for input
user_input = input('Please enter an IPV4 Ip address:' )

# Display information back to user
print('You told me the IPV4 IP address is:',  user_input)

# Prompt the user for the vendor name
vendor_input = input('Please provide the vendor name of the associated device: ')

# Display the vendor information back to the user
print('The vendor name is: ', vendor_input)
