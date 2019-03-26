n = int(input())
for i in range(n):
    d, s = input().split()
    d = int(d)
    res = ""
    for c in s:
        res += c*d
    print(res)