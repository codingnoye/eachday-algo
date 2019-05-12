import math
s,e=map(int,input().split())
def whatis(n):
    return math.ceil(((8*n)**0.5-1)/2)
r=0
for i in range(s,e+1):
    r+=whatis(i)
print(r)