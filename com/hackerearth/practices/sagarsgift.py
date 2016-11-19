'''
Created on 17-Nov-2016

@author: trinadhkoya
'''
N=int(input())
gift_data=list(map(int,input().split()))[:N]
s=sorted(gift_data)

for i in range(0,len(s)):
    print(s[i])