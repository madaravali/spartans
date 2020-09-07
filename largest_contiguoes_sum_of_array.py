a=[1,2,-2]
sum=0
sum1=0
l=[]
for i in a:
    sum=sum+i
for i in range(len(a)):
    sum1=sum1+a[i]
    if(sum1>=sum):
        l.append(sum1)
l.sort()
print(l[-1])
