#!/usr/bin/env python3

message = 'The grade you earned was '
grade = int(input('Please enter the score your earned on the test: '))
if grade >= 90:
    message = message + 'an A.'
elif grade >= 80:
    message = message + 'a B.'
elif grade >= 70:
    message = message + 'a C.'
elif grade >= 60:
    message = message + 'a D.'
else:
    message = message + 'an F.'
print(message)
    
