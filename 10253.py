from fractions import Fraction as fr
for i in range(int(input())):
    a, b = map(int, input().split())
    now = fr(a, b)
    while now.numerator != 1:
        a, b = now.numerator, now.denominator
        new = fr(a, a*(b//a+1))
        now = now - new
    print(now.denominator)