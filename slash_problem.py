c=int(input())
d=bin(c)
d=d.replace("0b","")
k=d[1:]+d[:1]
g=int(k,2)
print(g)
