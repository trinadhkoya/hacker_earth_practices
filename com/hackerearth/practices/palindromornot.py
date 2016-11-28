'''
Created on Nov 10, 2016

@author: trina
'''
s= str(input())
flag=0;

if s.isnumeric():
    for i in range(len(s)):
        if(s[i]==s[len(s)-i-1]):
                flag=1
        else:
            flag=0;
    if(flag==1):
        print("YES")
    else:
        print("NO")
else:
    print("please enter smaller letter")