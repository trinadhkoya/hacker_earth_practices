# '''
# Created on 30-Nov-2016

# @author: trinadhkoya
# '''
# sum=0
# str=list(map(str,input()))
# for char in range(len(str)):
#     sum+=(ord(str[char])-96)
# print(sum)
sum=0
str=str(input()).lower()
for char in str:
    sum+=ord(char)-96
print(sum)
