n,m,k=[int(x) for x in input().split()]
a=[int(i) for i in input().split()][:n]
b=[int(i) for i in input().split()][:m]
c=a+b
c.sort()
for i in range(len(c)):
    if(i==k):
        print(c[i-1])
