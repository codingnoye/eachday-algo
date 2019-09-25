import sys
sys.setrecursionlimit(10**6)
n = int(input())
board = list(map(
    lambda item: list(map(int, item.split())),
    sys.stdin.readlines()
    ))
now_board = []
mx = 0

def trace(x, y, h):
    global board, now_board
    if x<0 or x>=n or y<0 or y>=n: return
    if now_board[y][x] == 1: return
    if board[y][x] <= h: return
    now_board[y][x] = 1
    trace(x, y-1, h)
    trace(x-1, y, h)
    trace(x+1, y, h)
    trace(x, y+1, h)

for h in range(0, 101):
    count = 0
    now_board = [[0] * n for _ in range(n)]
    for y in range(n):
        for x in range(n):
            if board[y][x] > h and now_board[y][x]==0:
                trace(x, y, h)
                count += 1
    mx = max(count, mx)
    if count == 0:
        break
    #print(h, count)
print(mx)