N=int(input())
modulo=pow(10,9)+7
if (N>1)and(N<=pow(10,3)):
    array=list(map(int,input().split()))[:N]
    product=1
    for i in range(len(array)):
        product=(product*array[i])%modulo
    print(product)