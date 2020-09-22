arr=[int(x) for x in input().split()]
arr.sort()
i=0;
j=len(arr)-1;
sum=int(input());
k=int((j-1)/2);
while((i<j)&(i<k)&(k<j)):
    if((arr[i]+arr[j]+arr[k])<sum):
        i=i+1;
    elif((arr[i]+arr[j]+arr[k])==sum):
        print(i);
        print(j);
        print(k);
        j=j-1;
        k=k+1;
        if(k==j):break;
        if(i==k):break;
