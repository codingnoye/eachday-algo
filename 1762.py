n, m = map(int, input().split())
points = [[]for i in range(n+1)]
for i in range(m):
    s, e = map(int, input().split())
    points[s]+=[e]
    points[e]+=[s]
triangle = set()
for i in range(1, n+1):
    for j in points[i]:
        for k in points[j]:
            if i in points[k]:
                triangle.add(2**(i-1)+2**(j-1)+2**(k-1))
print(len(triangle))