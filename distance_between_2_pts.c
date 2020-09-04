#include<stdio.h>
#include<math.h>
struct point
{
	int x;
	int y;
};
int distance(int g,int e,int d,int f)
{
    int diz;
    diz=sqrt(((f-e)*(f-e))+((d-g)*(d-g)));
    printf("%d",diz);
}
int main()
{
  int d,e,f,g;
  struct point P1;
  struct point P2;
  P1.x=4;
  P1.y=7;
  P2.x=8;
  P2.y=7;
  distance(P1.x,P1.y,P2.x,P2.y);
}
