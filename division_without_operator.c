#include <stdio.h>
int main(void){
    // Your code here!
    long long int divisor,div,val=0,q=0,i;
    scanf("%lld%lld",&div,&divisor);
    for(i=31;i>=0;i--)
    {
        if(val+(divisor<<i)<=div)
        {
            val=val+(divisor<<i);
            q=q|(1<<i);
        }
    }
    printf("%lld",q);
}


