def call(n,g,d):
    if n>g:
        return 99999
    if n==g:
        return d
    return min(call(n*10+1,g,d+1),call(2*n,g,d+1))
r=call(*map(int,input().split()),1)
print(-1 if r==99999 else r)