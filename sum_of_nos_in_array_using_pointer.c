#include <stdio.h>
int main(void)
{
  int i,b[5],*d,sum=0;
  for(i=0;i<5;i++)
  {
    scanf("%d",&b[i]);
  }
  
  for(i=0;i<5;i++)
  {
     d=&b[i];
     sum=sum+*d;
  }
  printf("%d",sum);
  }
