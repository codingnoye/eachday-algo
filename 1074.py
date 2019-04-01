n, r, c = map(int, input().split())
count = 0
def f(n,x,y):
    global count, r, c
    if n>=1 and (c<x or r<y or c>=x+2**n or r>=y+2**n):
        count += (2**n)**2
        return
    if x==c and y==r:
        print(count)
        exit(0)
    elif n==0: count += 1
    if n>0:
        f(n-1, x, y)
        f(n-1, x+2**(n-1), y)
        f(n-1, x, y+2**(n-1))
        f(n-1, x+2**(n-1), y+2**(n-1))
f(n, 0, 0)