from collections import defaultdict
d = defaultdict(list)
temp=[]

n, m = map(int,input().split())

for i in range(0,n):
    d[input()].append(i+1) 

for i in range(0,m):
    list1=temp+[input()]
    
for i in temp:
    if i in d:
        print(" ".join(map(str,d[i])))
    else:
        print(-1)  

