a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
#1. Instead of printing the elements one by one, make a new list that has all the elements less than 5 from this list in it and print out this new list.
b = []
for e in a: 
    if e < 5: 
	    b.append(e)

print(b)
input('next?')

#2. Write this in one line of Python.
#for e in a if e < 5 b.append(e)
#sample solution says more knowledge needed to accomplish this


#3Ask the user for a number and return a list that contains only elements from the original list a that are smaller than that number given by the user.

num = int(input('Filter array of less than: '))
c = []
for e in a: 
    if e < num: 
	    c.append(e)

print(c)


input('end?')