a=int(input())
d=[int(i) for i in input().split()]
for i in range(len(d)):
    sum=d[i]
    for j in range(i+1,len(d)):
        sum=sum+d[j]
        if(sum==a):
            print(i)
            print(j)
        
        
