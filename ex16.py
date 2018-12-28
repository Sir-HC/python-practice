
import random


MIN_CHR_VAL = 32
MAX_CHR_VAL = 126

#Basic Latin Unicode Range: 32 - 126 -- See Wikipedia for range

#Valid Range 0 - 1114111 -- May cause instablility 


running = True

while running:
    _in = input('Length of Password or [Q]uit\n')
    try:
        _in = int(_in)
    except ValueError:
        if _in.upper() == 'Q':
            running = False
            continue
        else:
            print('Invalid entry')
            continue
    pswd = ''
    for x in range(0, _in):
        rndNum = random.randint(MIN_CHR_VAL, MAX_CHR_VAL)
        pswd = pswd + chr(rndNum)
    print(pswd)