'''
Created on 12-Nov-2016

@author: trinadhkoya
'''
list=[]
check=True
while check==True:
    n=int(input())
    if n==42:
        check=False
    else:
        list.append(n)
for i in list:
    print(i)