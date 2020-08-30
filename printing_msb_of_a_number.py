n=int(input())
k=bin(n)
k=k.replace("0b","")
t=k.replace("0","1")
g=int(t,2)
u=(g+1)/2
for i in range(10):
    if((2**i)==u):
        j=i
j=j+1 
print(j)
