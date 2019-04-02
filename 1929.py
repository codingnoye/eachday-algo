n, m = map(int, input().split())
sosu = [2]
for i in range(1, m+1):
    issosu = True
    for j in sosu:
        if j*j > i: break
        if i%j == 0:
            issosu = False
            break
    if issosu and i!=1:
        if i>=n: print(i)
        sosu.append(i)
