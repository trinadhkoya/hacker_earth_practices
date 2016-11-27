'''
Created on 23-Nov-2016

@author: trinadhkoya
'''


def check_count(str):
    k=0
    str=str
    str="--{}--".format(str)
    str=list(str)
    for i,j in enumerate(str):
        if str[i] == 'B':
            if str[i-1] == 'W':
                k += 1
                str[i-1] = '-'
            if str[i-2] == 'W':
                k += 1
                str[i-2] = '-'
            if str[i+1] == 'W':
                k += 1
                str[i+1] = '-'
            if str[i+2] == 'W':
                k += 1
                str[i+2] = '-'
    print(k)

T=int(input())
while T!=0:
    check_count(str(input()))
    T-=1
    
    
    
    
                

                
    
            
            
    
    
       
    
            
