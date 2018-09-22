#include<stdio.h>
#include<conio.h>
main()
{
    int i,j,k,n,m;
    printf("Enter the number of row : ");
    scanf("%d",&n);
    for(i=1;i<=n;i++)
    {
        for(j=n+2;j>=i;j=j-1)
        {
            printf(" ");
        }
        for(k=1;k<=i;k++)
        {
            printf("%d",k);
        }
        for(m=i;m>1;m--)
        {
            printf("%d",m-1);
        }
        printf("\n");
    }
    getch();
}
