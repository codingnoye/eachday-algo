n = int(input())
l = [['*' for j in range(n)] for i in range(n)]
i = 1
while i < n:
    for k in range(0, n, i):
        for m in range(i):
            if (k+m) // i % 3 == 1:
                for c in range(len(l[k+m])):
                    if (c // i % 3 == 1):
                        l[k+m][c] = ' '
    i *= 3
print('\n'.join(list(map(lambda x:''.join(x), l))))
