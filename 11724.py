import sys
sys.setrecursionlimit(10**6)
n, m = map(int, input().split())
points = [[] for i in range(n)]
for i in range(m):
    a, b = map(int, sys.stdin.readline().split())
    points[b-1].append(a-1)
    points[a-1].append(b-1)
for i in range(n):
    points[i] = list(set(points[i]))
mx = 1
visited = [0] * n

def visit(n, m):
    global visited, points
    if visited[n]: return
    visited[n] = m 
    for i in points[n]:
        if visited[i]: continue
        visit(i, m)

for i in range(n):
    if visited[i]: continue
    visit(i, mx)
    mx += 1

print(mx-1)