'''
Created on Nov 16, 2016

@author: trina
'''


# def product(N, values):
#     answer=1;
#     for i in range(N):
#         answer*=values[i]%(pow(10,9)+7)
#     return answer
#         
# 
# N=int(input())
# values=list(map(int,input().split()))[:N]
# 
# print(product(N,values))

def product(num,values):
    answer = 1
    for i in range(num):
        
        answer = answer*values[i] % pow(10,9)+7
        
    return answer
    
 
N= int(input())
 
values = list(map(int, input().split()))
answer = product(N,values)
print(answer)
 
