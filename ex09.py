#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 

import random

running = True

while running:
    uInput = input('Guess a number 1 to 9, or [Q]uit')
    if uInput.upper() == 'Q':
        running = False
        break
	
    uInput = int(uInput)
    cInput = random.randint(1,9)

    if uInput == cInput:
        #draw
        print('You won!')
    elif uInput > cInput:
        #uInput wins
        print('Too High!')
    elif uInput < cInput:
        #cInput wins
        print('Too Low!')	

input('exit')
