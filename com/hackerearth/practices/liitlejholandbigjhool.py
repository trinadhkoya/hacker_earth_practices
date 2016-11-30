'''
Created on Nov 30, 2016

@author: trina
'''
str=str(input())
check = str.find('111111') or str.find('000000')

if check>=0:
    print("Sorry sorry!")
else:
    print("Good Luck")
