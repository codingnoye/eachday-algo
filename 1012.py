import sys
sys.setrecursionlimit(10**6)
def check(x, y):
    global m, w, h
    if x < 0 or x == w:
        return
    if y < 0 or y == h:
        return
    if m[x][y] == 1:
        m[x][y] = 2
        check(x+1, y)
        check(x, y+1)
        check(x-1, y)
        check(x, y-1)
for case in range(int(input())):
    w, h, c = map(int, input().split())
    m = [[0 for i in range(h)] for j in range(w)]
    for i in range(c):
        x, y = map(int, input().split())
        m[x][y] = 1
    count = 0
    for y in range(h):
        for x in range(w):
            if m[x][y] == 1:
                count += 1
                check(x, y)
    print(count)