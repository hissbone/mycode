#!/usr/bin/env python3

proto = ['ssh', 'http', 'https']
protoa = ['ssh', 'http', 'https']

print(proto)
print(proto[1])
proto.append('dns')
protoa.append('dns')
print(proto)
proto2 = [22, 80, 443, 53 ]
proto.extend(proto2)
print(proto)
proto.append(proto2)
print(proto2)

# set a variable the show the number of time the string 'http' is present in proto
http_count = proto.count('http')
# print a message with the value of http_count
print('The count for http in proto is', http_count)
