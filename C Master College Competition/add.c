#include<stdio.h>
#include<conio.h>
void add(int a[],int b[],int n);
void main()
{
	int a[100],b[100],n,i;
	clrscr();
	scanf("%d",&n);
	for(i=0;i<n;i++)
	scanf("%d",&a[i]);
	for(i=0;i<n;i++)
	scanf("%d",&b[i]);
	add(a,b,n);

}
void add(int a[],int b[],int n)
{
	int c[100],i,j,sum,rem,div;
	for(i=0;i<n+1;i++)
	c[i]=0;
	for(i=n-1;i>=0;i--)
	{
		sum=a[i] + b[i];
		if( sum >=10 && i != 0)
		{
			rem  = sum % 10;
			div  = sum / 10;
			c[i] += rem;
			c[i-1]=div;
		}
		else
		{
			c[i]+=sum;
		}

	}
	for(i=0;i<n;i++)
	printf("%d ",c[i]);
	getch();

}
