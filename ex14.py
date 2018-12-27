#Write a program (function!) that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.

#Extras:

#Write two different functions to do this - one using a loop and constructing a list, and another using sets.
#Go back and do Exercise 5 using sets, and write the solution for that in a different function.

import pdb


a = [1,3,8,32,21,2,8,32,9,6,2,3,4]

def loopUnique(_list):
    res = []
    for ele in _list:
        if ele not in res:
            res.append(ele)
    print(res)
	
def setUnique(_list):
    res = set(_list)
    res = list(res)
    print(res)
	
def ex5Func(_a, _b):
    res = _a+_b
    res = set(res)
    res = list(res)
    print(res)

loopUnique(a)
setUnique(a)
#pdb.set_trace()
a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
ex5Func(a,b)

input('exit')