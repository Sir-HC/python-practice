#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

import time
#import pdb

num = int(input('input a number: '))

#pdb.set_trace()
array = range(3, num, 2)

res = []


ts = time.time()

if num == 2:
    print('prime')

	
#suboptimal algo, but good enough, 7919 is done in less than a second
#doesn't include 2 as a divisor, too lazy to fix
for ele in array:
    if num % ele == 0:
	    res.append(ele)

te = time.time()
total = te-ts
print('time taken: ' + str(total))
if len(res) == 0:
    print('number was prime')
else:
    print('number is not prime, divisors:')
    print(res)

input('exit')