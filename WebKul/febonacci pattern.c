#include<stdio.h>
#include<conio.h>
int f(int);
void main()
{
	int n,i,j,n1,p,k,l=0,n2;
	clrscr();
	scanf("%d",&n);
	if(n!=2)
	p = f(n)+2;
	else
	p=f(n);
	n2 = n;
	while(n2>1)
	{
		n1 = f(n2);
		for(j=0;j<n1;j++)
		{
			for(k=0;k<l;k++)
			{
				printf(" ");
			}
			printf("*");
			for(k=p;k>0;k--)
			{
				printf(" ");
			}
			//if(n1!=1)
			printf("*");
			printf("\n");
		}
		p-=2;
		l+=1 ;
		n2--;
	}
	n2 = n;
	for(i=0;i<l;i++)
	printf(" ") ;
	printf("*\n");

	n2=2;
	l=n-2;
	p=1;
	while(n2<n+1)
	{
		n1 = f(n2);
		for(j=0;j<n1;j++)
		{
			for(k=0;k<l;k++)
			{
				printf(" ");
			}
			printf("*");
			for(k=p;k>0;k--)
			{
				printf(" ");
			}
			//if(n1!=1)
			printf("*");
			printf("\n");
		}
		p+=2;
		l-=1 ;
		n2++;
		//printf("\n");
	}

	getch();

}
int f(int n)
{
	if(n == 1 || n == 2)
	return 1 ;
	else
	return(f(n-1) + f(n-2));
}
