n=[int(x) for x in input().split()]
print(n)
sum=0;
sum1=0;
for i in range(len(n)):
    if(i<(len(n)/2)):
        sum=sum+n[i];
    if(i>(len(n)-2)/2):
        sum1=sum1+n[i];
        if(sum==sum1):
            print(int((len(n)-1)/2));
        else:print(-1);   
