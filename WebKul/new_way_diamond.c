#include<stdio.h>
#include<conio.h>
void add(int a[],int b[],int n);
void main()
{
	int i,j,n=11,k,m=1,p,q;
	clrscr();
	k=n/2+n;
	p=n+1;
	q=n-2;
	for (i=0;i<n;i++)
	{
		if(i < n/2)
		{
			for(j=k;j>0;j--)
			{
			printf("  ");
			}
			for(j=0;j<m;j++)
			printf("* ");
			k--;
			m+=2;
		}
		else if(i > n/2)
		{
			for(j=p;j > 0;j--)
			{
				printf("  ");
			}
			for(j=q;j > 0;j--)
			printf("* ");
			q-=2;
			p++;
		}
		if(i == n/2)
		{
			for(j=0;j<n;j++)
			printf("@ ");
			for(j=0;j<n;j++)
			printf("* ");
			for(j=0;j<n;j++)
			printf("@ ");

		}

		printf("\n");

	}

	getch();

}



/*


input 3
- - - - *
@ @ @ * * * @ @ @
- - - - *


input 5

- - - - - - - *
- - - - - - * * *
@ @ @ @ @ * * * * * @ @ @ @ @
- - - - - - * * * 
- - - - - - - *

*/
