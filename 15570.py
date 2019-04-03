import sys
sys.setrecursionlimit(10^6)
n, m = map(int, input().split())
cache = 0
def fac(n):
    return (n*fac(n-1)) if n>1 else 1
def h(n, r):
    return int(int(fac(n+r-1) / fac(n)) / fac(r-1))
def check(n):
    global cache
    if cache == 0:
        for i in range(1, n+1):
            cache += h(n-i, i)
    return cache
queue = [(0, 1)]
count = 0
while queue:
    now = queue.pop(0)
    print('pop', now)
    if now[0] == m:
        count += now[1]
        print('end', now)
        continue
    for i in range(1, n+1):
        if now[0]+i > m:
            break
        queue.append((now[0]+i, now[1]))
        print('push', (now[0]+i, now[1]))
    if now[0]+n < m: queue.append((now[0]+n, now[1]*check(n)))
print(count%1999)
