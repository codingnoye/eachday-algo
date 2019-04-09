def gcd(a,b):
    return 1 if b==0 else gcd(b, a%b)
for c in range(int(input())):
    m, n, x, y = map(int, input().split())
    a = x
    mx = m*n
    while a<=mx:
        if (a-1) % n + 1 == y:
            print(a)
            break
        a += m
    else:
        print(-1)