import math
case = int(input())
for i in range(case):
    x, y = map(int, input().split())
    dis = y-x
    n = 1
    while (n+1)*(n+1) <= dis:
        n += 1
    diff = dis - n*n
    print(n + n - 1 + math.ceil(diff/n))
