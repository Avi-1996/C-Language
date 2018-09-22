#include<conio.h>
#include<stdio.h>
void main()
{
	int a,b,c,a1,b1,c1;
  printf("EDnter firest start time line with seprated space the In second line enter the end time in hrs min sec format");
	scanf("%d %d %d\n%d %d %d",&a,&b,&c,&a1,&b1,&c1);
	if(c1 < c)
	{
		--b1;
		c1+=60;
		c1 -= c ;
	}
	if(b1 < b)
	{
		--a1;
		b1 += 60;
		b1 -= b ;
	}
  
	printf("\n Doffrence Time \n %d %d %d",a1-a,b1,c1);
	getch();
}
