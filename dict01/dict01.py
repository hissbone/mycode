#!/usr/bin/env python3

# create a dictionary
switch = {'hostname': 'sw1','ip': '10.0.1.1', 'version': '1.2', 'vendor': 'cisco'}

#display part of the dictionary
print(switch['hostname'])
print(switch['ip'])

##request a fake key
#print(switch['faux'])


#request a fake key with a .get() method
print('First test - .get()')
print(switch.get('lynx'))

print('Second test - .get()')
print(switch.get('lynx', "The key is another castle!"))

print('Third test - .get()')
print(switch.get('version'))

print('Fourth test - .keys()')
print(switch.keys())

print('Fifth test - .values()')
print(switch.values())


print('Sixth test - .pop()')
print(switch.pop('version'))
print(switch.keys())
print(switch.values())


print('Seventh test - Add new value')
switch['adminlogin'] = 'karl08'
print(switch.keys())
print(switch.values())

print('Eighth test - Add new value')
switch['password'] = 'qwerty'
print(switch.keys())
print(switch.values())
