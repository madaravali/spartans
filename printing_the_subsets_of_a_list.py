n=int(input())
a=[]
for i in range(n):
    i=int(input())
    a.append(i)
t=[]
for i in range(0,2**(len(a))):
    h=[]
    for j in range(len(a)):
         if((i&(1<<j))==(1<<j)):
             h.append(a[j])
    t.append(h)
print(t)
