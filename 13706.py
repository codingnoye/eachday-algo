import math
n = int(input())
s, e = 0, 10**(int(math.log10(n))//2+1)
while True:
    m = (s+e)//2
    m2 = m**2
    if m2==n:
        print(m)
        exit(0)
    elif m2>n:
        s, e = s, m
    else:
        s, e = m+1, e