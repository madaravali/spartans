a=[int(x) for x in input().split()]
h=[]
for i in range(len(a)):
    if(i==0):h.append(a[0:-1])
    else:h.append(a[i:]+a[:i-1])
l=[]
for i in range(len(a)):
    sum=0
    for j in range(len(a)-1):
        sum=sum+h[i][j]
    l.append(sum)
l.sort()
print(l[-1])
