import sys
sosu = [2, 3, 5]
n = int(input())
inp = []
for C in range(n):
    inp.append(int(sys.stdin.readline()))
mx = max(inp)
mn = min(inp)
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
for a in range(len(sosu)):
    if sosu[a]+sosu[a]+sosu[a]>mx: break
    for b in range(a, len(sosu)):
        if sosu[a]+sosu[b]+sosu[b]>mx: break
        for c in range(max(tool[min(sosu[len(sosu)-1], max(mn-sosu[a]-sosu[b], 0))], b), len(sosu)):
            s = sosu[a]+sosu[b]+sosu[c]
            if s>mx: break
            if sosu[a]+sosu[b]<=sosu[c]: break
            count[s] += 1
for i in inp:
    sys.stdout.write(str(count[i])+'\n')