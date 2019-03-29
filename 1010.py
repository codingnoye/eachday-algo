def fac (n) :
    if n <= 1:
        return 1
    return n * fac(n-1)
for i in range(int(input())):
    a, b = map(int, input().split())
    print(fac(b)//fac(b-a)//fac(a))