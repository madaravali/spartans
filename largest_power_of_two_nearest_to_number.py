n=int(input())
k=bin(n)
k=k.replace("0b","")
t=k.replace("0","1")
g=int(t,2)
i=(g+1)/2
print(int(i))
