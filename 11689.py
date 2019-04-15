n = int(input())
if n==1:
    print(1)
    exit(0)
li = []
for i in range(2, n+1):
    if n%i == 0:
        li.append(i)
print(li)
sosu = []
for i in li:
    issosu = True
    for j in range(2, i):
        if j*j>i: break
        if i%j == 0:
            issosu = False
            break
    if issosu:
        if not i in sosu: sosu.append(i)           
print(sosu)
k = n
for i in sosu:
    k -= n // i
print(int(k))