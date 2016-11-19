'''
Created on 12-Nov-2016

@author: trinadhkoya
'''
n=int(input())


def fact(n):
    if(n<=1):
        return n
    else:    
        return n*fact(n-1);
print(fact(n))