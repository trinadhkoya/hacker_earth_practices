

def max_number(data):
    temp="";
    for i in range(len(data)):
        temp+=str(values[i]);
    return "".join(sorted(temp, reverse=True));

N=int(input())
for i in range(0,N):
    T=int(input())
    values=list(map(int,input().split()))[:T]
    print(max_number(values))
    