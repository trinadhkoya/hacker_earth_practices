'''
Created on 17-Nov-2016

@author: trinadhkoya
# '''

# 
# for i in  range(int(input())):
#     actual_str=str(input())
#     reversed_str=actual_str[::-1]
#     output_string=""
#     actual_str_split=list(actual_str)
#     reversed_str_split=list(reversed_str)
#     for j in range(len(actual_str)):
#         actual_str_ord=ord(actual_str[j])-96
#         reversed_str_ord=ord(reversed_str[j])-96
#         concat_of_both=actual_str_ord+reversed_str_ord
#         if concat_of_both>26:
#             concat_of_both=concat_of_both-26
#         char=chr(concat_of_both+96)
#         output_string=output_string+char
#     print(output_string)
#     

def doAction(key_board_input):
    actual_str=key_board_input
    reversed_str=actual_str[::-1]
    output_string=""
    actual_str_split=list(actual_str)
    reversed_str_split=list(reversed_str)
    for j in range(len(actual_str)):
        actual_str_ord=ord(actual_str[j])-96
        reversed_str_ord=ord(reversed_str[j])-96
        concat_of_both=actual_str_ord+reversed_str_ord
        if concat_of_both>26:
            concat_of_both=concat_of_both-26
        char=chr(concat_of_both+96)
        output_string=output_string+char
    print(output_string)
    



N=int(input())
while N!=0:
    doAction(str(input()))
    N=N-1

        
# def doAction(string):
#     
#     reversed_string=string[::-1]
#     list=[]
#     new=""
#     for i in range(len(string)):
#         s1=ord(string[i])-96
#         s2=ord(reversed_string[i])-96
#         temp=s1+s2
#         if temp>26:
#             temp=temp-26
#             
#         temp=chr(temp+96)
#         new+=temp
#         
#         return temp
#         
# #         list.append(temp)
# #     for item in list:
#        # print(chr(int(item))
#        
#     #print(list)
#         
#         
#         
#         
#         
#         
#     
#     
#     
# N=int(input())
# while N!=0:
#     _str=str(input())
#     doAction(_str)
#     N=N-1