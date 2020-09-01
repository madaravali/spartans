n=int(input())
a=[]
for i in range(n):
     i=int(input())
     a.append(i)
sum=0
t=0
for i in range(0,len(a)):
    sum=sum+a[i]
    if(sum>=5):
        sum=a[i]
        t=t+1
if(sum<5):
    t=t+1
print(t)
