n = int(input())
ltrb = [0]*(2*n-1)
lbrt = [0]*(2*n-1)
row = [0]*n
res = 0
def trace(x, y):
    global n, ltrb, lbrt, row, res
    if y<0 or y>=n: return
    if row[y] or ltrb[n-1+x-y] or lbrt[x+y]:
        return
    else:
        if x==n-1: 
            res += 1
            return
        row[y], ltrb[n-1+x-y], lbrt[x+y] = 1, 1, 1
        [trace(x+1, i) for i in range(0, max(y-1,0 ))]
        [trace(x+1, i) for i in range(min(n-1, y+2), n)]
        row[y], ltrb[n-1+x-y], lbrt[x+y] = 0, 0, 0
        return
[trace(0, i) for i in range(0, n)]
print(res)