'''
Created on Nov 30, 2016

@author: trina
'''

N=int(input())

if 1<=N<=pow(10,6):
    Str=list(map(str,input().lower()))[:N]
    Str_h_count=Str.count("h")//2;
    Str_a_count=Str.count("a")//2;
    Str_c_count=Str.count("c");
    Str_k_count=Str.count("k");
    Str_e_count=Str.count("e")//2;
    Str_r_count=Str.count("r")//2;
    Str_t_count=Str.count("t");
    
    print(min(Str_h_count,Str_a_count,Str_c_count,Str_k_count,Str_e_count,Str_r_count,Str_t_count))

