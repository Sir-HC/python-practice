#Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input), compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

import random

running = True

#    x beats x+1
inputs = ['R', 'S', 'P']


while running:
    uInput = input('[R]ock, [P]aper, [S]cissors, [Q]uit').upper()
    if uInput == 'Q':
        running = False
        break
	
    uInput = inputs.index(uInput)
    cInput = random.randint(0,2)

#Debug	
#    print('User: ' + str(uInput))
#    print('Comp: ' + str(cInput))
    if uInput == cInput:
        #draw
        print('Draw!')
    elif (uInput+1)%3 == cInput:
        #uInput wins
        print('User wins!')
    elif (cInput+1)%3 == uInput:
        #cInput wins
        print('Computer wins!')	

#for x in range(10):
#    num = random.randint(1,3)
#    print(num)

#input('exit')