sosus = [2]
res = []
m = int(input())
n = int(input())
if m<=2 and n>=2:
    res.append(2)
for i in range(2, n+1):
    issosu = True
    for sosu in sosus:
        if i%sosu == 0:
            issosu = False
    if issosu:
        sosus.append(i)
        if i>=m:
            res.append(i)
if len(res):
    print(sum(res))
    print(min(res))
else:
    print(-1)