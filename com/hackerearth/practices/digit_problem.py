'''
Created on 02-Dec-2016

@author: trinadhkoya
'''
# 
# X,K=input().split()
# X=[int(i) for i in X]
# K=int(K)
# largest_num=[]
# max_value=9
# for j in X:
#     if(K>0):
#         if(j<9):
#             largest_num.append(max_value)
#             K-=1
#         else:
#             largest_num.append(str(j))
#     else:
#         largest_num.append(str(j))
# print(*largest_num,sep='')
#             
#             




X,K = input().split()
K = int(K)
largest_num = ""
 
for i in X:
    
  if i != '9' and K != 0:

    K -= 1
    largest_num += '9'
  else:
    print(largest_num)
    largest_num += i

print (largest_num)