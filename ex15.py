#Write a program (using functions!) that asks the user for a long string containing multiple words. Print back to the user the same string, except with the words in backwards order.


string = input('input a few words: ')

_list = string.split(' ')

_list = _list[::-1]
res = ''
for ele in _list:
    res += ele + ' '

print(res)
input('exit')	