divisor=int(input())
divident=int(input())
val=0
q=0
for i in range(0,31):
    if(val+(divisor<<i)<=divident):
        val=val+(divisor<<i)
        q=q|(1<<i)
print(q)
