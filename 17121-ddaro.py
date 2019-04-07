import sys
sosu = [2, 3, 5]
n = int(input())
inp = list(map(int, sys.stdin.readlines()))
mx = max(inp)
count = [0 for i in range(mx+1)]
for i in range(6, mx-3):
    issosu = True
    for j in sosu:
        if j*j>i:break
        if i % j == 0:
            issosu = False
            break
    if issosu: sosu.append(i)
tool = []
ii=1
jj=0
while jj<len(sosu):
    tool.append(jj)
    if ii>sosu[jj]:
        jj+=1
    ii+=1
def tr(n):
    global sosu, tool
    count = 0
    for a in range(len(sosu)):
        if sosu[a]+sosu[a]+sosu[a]>n: break
        for b in range(a, len(sosu)):
            if sosu[a]+sosu[b]+sosu[b]>n: break
            for c in range(max(tool[min(sosu[len(sosu)-1], max(n-sosu[a]-sosu[b], 0))], b), len(sosu)):
                s = sosu[a]+sosu[b]+sosu[c]
                if s>n: break
                if sosu[a]+sosu[b]<=sosu[c]: break
                if n==s: count += 1
    sys.stdout.write(str(count)+',')
for i in inp:
    if i%2 == 1:
        tr(i)