n, m = map(int, input().split())
grid = [list(map(int,input())) for i in range(n)]
visited = [[False for j in range(m)] for i in range(n)]
arrive = 4200000000
def dfs (x,y,c):
    global arrive
    if x<0 or x>=m or y<0 or y>=n: return
    if grid[y][x] == 0 or visited[y][x]: return
    if x==m-1 and y==n-1:
        if arrive>c:
            arrive = c
    visited[y][x] = True
    dfs(x+1, y, c+1)
    dfs(x, y+1, c+1)
    dfs(x-1, y, c+1)
    dfs(x, y-1, c+1)
    visited[y][x] = False
dfs(0,0,1)
print(arrive)