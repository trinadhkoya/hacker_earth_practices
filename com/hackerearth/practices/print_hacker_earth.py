'''
Created on Nov 30, 2016

@author: trina
'''

N=int(input())
input_=list(map(str,input().lower()))[:N]
print (min((input_.count("h")//2, input_.count("a")//2, input_.count("c"), input_.count("k"),input_.count("e")//2,input_.count("r")//2, input_.count("t"))))
