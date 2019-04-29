n, m = map(int, input().split())
grid = [[0 for i in range(m+2)]]+[list(map(int,'0'+input()+'0')) for i in range(n)]+[[0 for i in range(m+2)]]
queue = []
queue.append((1, 1, 1))
while True:
    x,y,c = queue.pop(0)
    if x==m and y==n:
        print(c)
        break
    if grid[y][x+1]:
        queue.append((x+1, y, c+1))
        grid[y][x+1] = 0
    if grid[y+1][x]:
        queue.append((x, y+1, c+1))
        grid[y+1][x] = 0
    if grid[y][x-1]:
        queue.append((x-1, y, c+1))
        grid[y][x-1] = 0
    if grid[y-1][x]:
        queue.append((x, y-1, c+1))
        grid[y-1][x] = 0