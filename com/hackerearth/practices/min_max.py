'''
Created on 16-Nov-2016

@author: trinadhkoya
'''
from array import array


N=int(input())
array=list(map(int,input().split()))[:N]
array.sort()
array2=list(range(min(array),max(array)+1))
if set(array)==set(array2):
    print("YES")
else:
    print("NO")



# N=int(input())
# array_1=list(map(int,input().split()))[:N]
# array_temp=[i for i in range(min(array_1),max(array_1)+1)]
# flag=0
# for x in array_temp:
#      if x not in array_1:
#          flag=1
# 
# if(flag):print("NO")
# else:print("YES")
