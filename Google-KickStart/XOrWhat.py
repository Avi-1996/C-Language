def  countSetBits(n): 
    count = 0
    while (n): 
        count += n & 1
        n >>= 1
    return count 
def checkeven(li,start,end):
    x =0
    for o in range(start,end):
        x^=li[o]
    return countSetBits(x)
case = int(input())
for u in range(case):
    finAns = [ ]
    n,q = list(map(int,input().split()))
    li = list(map(int,input().split())) 
    for _ in range(q):
        i,v = list(map(int,input().split()))
        li[i] = v
        ans = [ ]
        for k in range(len(li),0,-1):
            if(checkeven(li,0,k) % 2 == 0):
                ans.append(str(k))
        finAns.append(max(ans))
    if(len(finAns) > 0):
        print("Case #"+str((u+1)) +": " + " ".join(finAns))
    else:
        print("Case #"+str((u+1)) +": 0")
