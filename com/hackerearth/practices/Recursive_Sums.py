T=int(input())
for i in range(T):
    M=int(input())
    sum=0
    for _ in range(M):
        dl=input().split()
        sum+=int(dl[0])*int(dl[1])
    
    
    if(sum==0):
        print ("0")
    elif(sum%9==0):
        print("9")
    else:
        print(sum%9)