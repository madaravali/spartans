a=[int(x) for x in input().split()]
count=0
a.sort()
sum=0
for i in range(len(a)):
    for j in range(i+1,len(a)):
        if(j+1<len(a)):d=a[j+1]
        sum=a[i]+a[j]
        if(sum==d):count=count+1
        if(sum>d):i=i+1
        if(sum<d):d=a[j+2]
print(count) 
