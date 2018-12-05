#!/usr/bin/env python3

round = 0
while(True):
    round = round +1
    print('Finish the movie title, "Monty Python\'s, the life of ________"')
    answer = input().capitalize()
    if answer == 'Brian':
        print('That is correct!')
        break
    elif answer =='Shruberry':
        print('That is the supper secret answer!')
        break
    elif(round==3):
        print('Sorrry the answer was Brian')
        break
    else:
        print('Sorry, try again.')

