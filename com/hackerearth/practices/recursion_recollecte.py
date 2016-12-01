'''
Created on 24-Nov-2016

@author: trinadhkoya
'''


def fib(x):
        if x==1:
            return x
        else:
            return x*fib(x-1)




n=int(input())
print(fib(int(n)))