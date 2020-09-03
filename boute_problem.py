d=[]
d=[int(x) for x in input().split()]
d.sort()
j=d[0]
if(j==0):
    for i in range(len(d)):
        if(d[i]==0):
            i=i+1
            t=d[i]
            d[i]=d[0]
            d[0]=t
sum=0
y=len(d)
for i in range(len(d)):
    sum=sum+(d[i]*(10**(y-i-1)))
print(sum)  
