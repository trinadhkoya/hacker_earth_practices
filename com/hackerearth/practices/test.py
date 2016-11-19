'''
Created on 19-Nov-2016

@author: trinadhkoya
'''
for _ in range(input()):
    l_string=input()
    l_revString = ''.join(reversed(l_string))
    l_newString = ""
    l_string = list(l_string)
    print(l_string)
    l_revString = list(l_revString)
    for l_index in range(len(l_string)):
        l_ord =  ord(l_string[l_index]) - 96
        l_revord = ord(l_revString[l_index]) - 96
        l_neword = int(l_ord) + int(l_revord)
    #    print l_ord,l_revord,l_neword
        if l_neword > 26 :
            l_neword = l_neword - 26
 
        l_newAlpha = chr(l_neword+96)
 
        l_newString += l_newAlpha
 
    print (l_newString)