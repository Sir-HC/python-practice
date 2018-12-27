#Generate a random number between 1 and 9 (including 1 and 9). Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right. 
#Keep the game going until the user types “exit”
#Keep track of how many guesses the user has taken, and when the game ends, print this out.

import random

running = True

guesses = 0

while running:
    uInput = input('Guess a number 1 to 9, or [Q]uit')
    if uInput.upper() == 'Q':
        running = False
        break
	
    uInput = int(uInput)
    cInput = random.randint(1,9)
    guesses += 1

    if uInput == cInput:
        #draw
        print('You won!')
    elif uInput > cInput:
        #uInput wins
        print('Too High!')
    elif uInput < cInput:
        #cInput wins
        print('Too Low!')	

print("Guesses: " + str(guesses))
input('exit')
