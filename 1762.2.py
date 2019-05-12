n, m = map(int, input().split())
points = [[]for i in range(n+1)]
#lines = []
for i in range(m):
    s, e = map(int, input().split())
    points[s] += [e]
    points[e] += [s]
    #lines.append(2**(s-1)+2**(e-1)) 
triangle = set()
for i in range(1, n):
    for j in range(len(points[i])-1):
        for k in range(j+1, len(points[i])):
            #if 2**(points[i][j]-1)+2**(points[i][k]-1) in lines:
            #    triangle.add(2**(i-1)+2**(points[i][j]-1)+2**(points[i][k]-1))
            if points[i][j] in points[k]: triangle.add(2**(i-1)+2**(points[i][j]-1)+2**(points[i][k]-1))
print(len(triangle))