a=int(input())
d=[int(i) for i in input().split()]
for i in range(len(d)):
    for j in range(i+1,len(d)):
        sum=d[i]
        sum=sum+d[j]
        if(sum==a):
            print(i)
            print(j)
        if(sum>a):
            i=i+1
            continue
        
