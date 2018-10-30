#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 30 15:50:40 2018

@author: student
"""
n=4;
k=1;
for i in range(n):
    for j in range(n):
        print("- ",end='')
    print("*")
for i in range(n):
    for j in range(n-1,i,-1):
        print("- ",end='')
    for j in range(k):
        if i==0 and j ==0:
            print("* *",end='')
            break
        else:
            print("* ",end='')
    k+=2
    print()
k=n+1
for i in range(n-1):
    for j in range(i+1):
        print("- ",end='')
    for j in range(k):
        if i == n-2:
            print("* *",end='')
        else:
            print("* ",end='')
    k-=2
    print()
for i in range(n):
    for j in range(n):
        print("- ",end='')
    print("*")
    
    
''''
n=4
- - - - *
- - - - *
- - - - *
- - - - *
- - - * *
- - * * * 
- * * * * * 
* * * * * * * 
- * * * * * 
- - * * * 
- - - * *
- - - - *
- - - - *
- - - - *
- - - - *


'''''
