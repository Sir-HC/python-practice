#Write a program that asks the user how many Fibonnaci numbers to generate and then generates them. Take this opportunity to think about how you can use functions. Make sure to ask the user to enter the number of numbers in the sequence to generate

fib = [1,1]

num = int(input('how many fibb nums to calc?')) - 2

def fibb(fib, tar):
    #print(fib)
    if tar > 0:
        fib.append(fib[len(fib)-2] + fib[len(fib)-1])
        fibb(fib, tar-1)
    else:  
        return 

fibb(fib, num)
print(fib)

input('exit')