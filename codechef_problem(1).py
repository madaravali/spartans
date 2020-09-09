n,k=map(int,input().split())
a=[int(x) for x in input().split()]
b=[]
l=[]
for i in range(k):
    b=b+a
for i in range(len(b)):
    sum=b[i]
    for j in range(i+1,len(b)):
        if(sum>0):
            if(b[j]<0):
                i=i+1
                break
            if(b[j]>0):
                sum=sum+b[j]
                l.append(sum)
l.sort()
print(l[-1])
