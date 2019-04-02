n, m, v = map(int, input().split())
points = [[] for i in range(n)]
visited = [0 for i in range(n)]
printer = ""
for i in range(m):
    a, b = map(int, input().split())
    points[a-1].append(b - 1)
    points[b-1].append(a - 1)
for i in points:
    i.sort()
def dfs(now):
    global points, visited, printer
    if visited[now]:
        return
    visited[now] = 1
    printer += str(now+1) + " "
    for i in points[now]:
        dfs(i)
dfs(v-1)
print(printer[:-1])
printer = ""
queue = [v-1]
while queue:
    now = queue.pop(0)
    if visited[now] == 2:
        continue
    visited[now] = 2
    printer += str(now+1) + " "
    for i in points[now]:
        if visited[i] == 1: queue.append(i)
print(printer[:-1])