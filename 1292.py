s,e,c,n=int(input()),int(input()),0,0
for i in range(1,e+1):
    while True:
        if s<=i:
            c+=i
        n+=1
        if n==i:
            i=0
            break
print(c)