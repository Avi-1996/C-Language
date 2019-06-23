'''
Problem : given a n * n matrix and find the minumum elment 
among all the element which occur 4 times in a sequence eigthe in vertically ,horizontally,digonally
'''
n = 5
l = [
    [ 4 , 4 , 4 , 4 , 9 , 1 ], 
    [ 1 , 0 , 4 , 9 , 1 , 9 ],
    [ 2 , 1 , 9 , 1 , 3 , 9 ],
    [ 2 , 9 , 1 , 0 , 9 , 9 ],
    [ 2 , 9 , 3 , 1 , 0 , 9 ],
    [ 2 , 1 , 9 , 1 , 0 , 7 ],
]
'''
For above input
elemnet 4 appears 4 time horizontally in firs row
element 2 appears 4 times vertically in first column
element 1 appear 4 times in diagonally starting from first column and second row
element 1 appear 4 times in diagonally starting from 5th column and first row
element 9 appears 4 times vertically starting in first column

among All 1 is the minimum so the answer is 1 

if there is no such elements then print -1
'''

'''
[
    [ (0,0) , (0,1) , (0,2) , (0,3) , (0,4) , (0,5) ], #
    [ (1,0) , (1,1) , (1,2) , (1,3) , (1,4) , (1,5) ],
    [ (2,0) , (2,1) , (2,2) , (2,3) , (2,4) , (2,5) ],
    [ (3,0) , (3,1) , (3,2) , (3,3) , (3,4) , (3,5) ],
    [ (4,0) , (4,1) , (4,2) , (4,3) , (4,4) , (4,5) ],
    [ (5,0) , (5,1) , (5,2) , (5,3) , (5,4) , (5,5) ],
]

idea is to traverse the right Upper diagonal and right lower digonal elemnt and do it vice same as left diagonal element

after that w just need to traverse the virtically and horizontally and check the 4 consecutive element at the same time

print the smallest consecutive number that arrived 4 times in a sequence
'''

num = 4
conse =[ ]
small = set()
def checkForConsecutives(li):
    flag = False
    for i in range(0,len(li) - 3):
        flag = False
        for j in range(1,4):
            if(li[i] != li[i+j]):
                flag = True
                break;
        if not flag:
            small.add(li[i])
def LeftDiagonal(l):
    i,j,k,=0,0,0
    while(i<n+1):
        k=i
        j=0
        conse = [] 
        while(j<=i and k>=0):
            conse.append(l[k][j])
            j+=1
            k-=1
        i+=1
        if(len(conse) >= 4):
            checkForConsecutives(conse)
    i,j,k,=0,0,0
    while(i<n+1):
        k=i
        j=n
        conse = [] 
        while(j>=i-1 and k<=n):
            conse.append(l[k][j])
            j-=1
            k+=1
        i+=1
        if(len(conse) >= 4):
            checkForConsecutives(conse)
        print(conse)
        
def RightDiagonal(l):
    m,j,k=0,0,0
    i =n
    while(i>=0):
        k=i
        j=0
        conse = [] 
        while(j<=m and k<=n):
            print((j,k))
            conse.append(l[k][j])
            j+=1
            k+=1
        i-=1
        m+=1
        if(len(conse) >= 4):
            checkForConsecutives(conse)
    j,k=0,0
    i,m =n,n
    while(i>=0):
        k=i
        j=m
        conse = [] 
        while(j>=0 and k>=0):
            conse.append(l[k][j])
            j-=1
            k-=1
        i-=1
        if(len(conse) >= 4):
            checkForConsecutives(conse)
def HorZontal(li):
    for i in li:
        checkForConsecutives(i)
def Vertical(li):
    for i in range(0,len(li)):
        for j in range(0,len(li)):
            conse.append(li[j][i])
        checkForConsecutives(conse)
LeftDiagonal(l)
RightDiagonal(l)
HorZontal(l)
Vertical(l)
Vertical(l)
print(small)
# Now print the result if any other print -1
print(min(small)) if small else print("-1")
