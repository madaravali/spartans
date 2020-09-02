a=33
d=[1,4,20,3,10,5]
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
