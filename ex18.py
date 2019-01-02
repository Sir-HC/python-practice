#Randomly generate a 4-digit number. Ask the user to guess a 4-digit number. For every digit that the user guessed correctly in the correct place, they have a “cow”. For every digit the user guessed correctly in the wrong place is a “bull.” Every time the user makes a guess, tell them how many “cows” and “bulls” they have. Once the user guesses the correct number, the game is over. Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.

#didn't sum up number of guesses, got distrought using n^2 validation, probably would be quicker using some sort of mapping?

import random


running = True
    

def getInput():
    validChk = True
    while validChk:
        try:
            _guess = input('Input a 4 digit number, Q to exit:\n')
            if _guess.upper() == "Q":
                return "Q"
            int(_guess)
            if len(_guess) != 4:
                raise ValueError
            #we have an int with 4 numbers
            validChk = False
            
        except ValueError:
            print('Invalid entry, try again:\n')
    return _guess
            
while running:
    print("===Cows & Bulls===")
    game = True
        
    rndNum = random.randint(0,9999)
    rndNum = str(rndNum).rjust(4,'0')
    
    #Comment out for authentic experience!
    print('Answer: ' + rndNum)
    #=====================================
    
    while game:
    
        guess = getInput()
        
        if guess == "Q":
            game = False
            running = False
            continue
        
        if rndNum == guess:
            game = False
            print('You win!')
            continue
        cows = 0
        bulls = 0
        
        rndManip = rndNum
        
        for x in range(0,4):
            if rndNum[x] == guess[x]:
                cows += 1
                rndManip = list(rndManip) 
                rndManip[x] = 'x'
                rndManip = ''.join(rndManip)
                
        for x in range(0,4):
            if guess[x] in rndManip and guess[x] != rndNum[x]:
                bulls += 1
                
        print("Correct number in correct place, Cows: " + str(cows))
        print("Correct number in the wrong place, Bulls: " + str(bulls))
        
        print('Try again!')

input('exit')