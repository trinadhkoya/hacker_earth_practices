'''
Created on 03-Dec-2016

@author: trinadhkoya
'''
import sys
sys=sys.setrecursionlimit(2000)

def func(x,y):
    if x==0:
        return (y+1)%1000
    elif x==1:
        return (y+2)%1000
    elif(y==0):
        return func(x-1, 1)%1000
    else:
        par2=func(x,y-1)%1000
        return func(x-1,par2)%1000

x,y=[int(i) for i in input().split()]
result=func(x,y)

output=str(result%1000)
while len(output)<3:
    output="0"+output
print(output)

