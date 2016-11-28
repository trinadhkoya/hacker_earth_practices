'''
Created on Nov 16, 2016

@author: trina
'''
import sys

ip=sys.stdin.read()
ip=ip.split()
ip=[int(i) for i in ip]
count=0

l,r,k=ip[0],ip[1],ip[2]

for i in range(l,r+1):
    if(i%k==0):count+=1
print(count)