'''
n = 3
---*
@@@**
---*

n = 5
-----*
-----**-----*
@@@@@***-@@@**
-----**-----*
-----*

n = 7
-------*
-------**-------*
-------***------**----*
@@@@@@@****@@@@@***@@@**
-------***------**----*
-------**-------*
-------*

'''
n = int(input())
def star(n,m):
    print("*"*n + " "*m,end = '')
def space(n):
    print(" "*n,end = '')
def atThe(n):
    print("@"*n,end = '')
k = n
sp= 1
m = 1
o = 1
spp = n//2
lowerstar = n//2
lowerspace = 1
lowerNoOfBlock = n//2
for i in range(1,n+1):
    if(i == n//2+1):
        o= n//2+1
        l = n
        s = n//2
        while(s>0):
            atThe(l)
            star(o,0)
            o-=1
            s-=1
            l-=2
    elif i<n//2+1:
        k = n
        l = o
        s = spp
        for j in range(1,sp+1):
            space(k)
            star(l,s)
            l-=1
            k-=2
        sp+=1
        spp-=1
        o+=1
    else:
        k = n
        l = lowerstar
        s = lowerspace
        for j in range(1,lowerNoOfBlock+1):
            space(k)
            star(l,s)
            l-=1
            k-=2
        lowerstar -= 1
        lowerspace +=1
        lowerNoOfBlock-=1
    print()
