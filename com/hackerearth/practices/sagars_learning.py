'''
Created on 19-Nov-2016

@author: trinadhkoya
'''
for _ in range(int(input())):
    number = int(input())
    number = number // 3
    if(number == 0):
        print(-1)
    else:
        print(number,number*2,number*3)
    
