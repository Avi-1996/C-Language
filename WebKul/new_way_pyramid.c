/*
n = 5
--@
--@
--@
--@
--@
*****
-***
--*
--@
--@
--@
-***
--*
n  = 7
---@
---@
---@
---@
---@
---@
---@
*******
-*****
--***
---*
---@
---@
---@
--***
---*
---@
---@
---@
---@
---@
-*****
--***
---*
---@
---@
---@
--***
---*

*/
#include<stdio.h>
void prr(int m,int n){
    int i,j,l,p;
    for(i=0;i<n;i++){
        for(j=0;j<m;j++){
            printf(" ");
        }
        printf("@");
        printf("\n");
    }
}
void star(int m ,int n){
    int i,j,k;
    k = n;
    for(i=0;i<n/2+1;i++){
        for(j=0;j<m;j++){
            printf(" ");
        }
        for(j=0;j<k;j++){
            printf("*");
        }
        k-=2;
        m++;
        printf("\n");
    }
}
int main(){
    int n,i,j,k,m,s,l,o;
    scanf("%d",&n);
    s=n/2+1;
    l=n;
    o=n/2;
    k=0;
    while(s>1){
    prr(o,l);
    star(k,l);
    l-=2;
    s--;
    k++;
    }
    

    return 0;
}

