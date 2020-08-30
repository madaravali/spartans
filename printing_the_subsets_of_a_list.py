a=[1,2,3]
t=[]
for i in range(0,8):
    h=[]
    for j in range(len(a)):
         if((i&(1<<j))==(1<<j)):
             h.append(a[j])
    t.append(h)
print(t)
