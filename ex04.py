#Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

num = int(input('input a number: '))

array = range(1, num +1)

res = []

for ele in array:
    if num % ele == 0:
	    print('added'+ str(ele))
	    res.append(ele)

print(res)
input('exit')