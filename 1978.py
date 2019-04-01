input()
count = 0
for i in list(map(int, input().split())):
    issosu = True
    if i == 1: continue
    for k in range(2, int(i**(1/2))+1):
        if i % k == 0:
            issosu = False
            break
    if issosu: count += 1
print(count)