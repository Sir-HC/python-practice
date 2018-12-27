#write a program that returns a list that contains only the elements that are common between the lists (without duplicates). Make sure your program works on two lists of different sizes. Write this in one line of Python using at least one list comprehension.


import random

size = random.randint(1, 20)
a = []
for x in range(size):
    a.append(int(random.randint(0,20)))

size = random.randint(1, 20)
b = []
for x in range(size):
    b.append(int(random.randint(0,20)))
	
#would need to remove duplicates, can't do an assign and check in same comprehension
res = [num for num in a if num in b]

print(a)
print(b)
print(res)
input('exit')