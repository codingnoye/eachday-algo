n = int(input())
i = 1
count = 0
while n > count:
    count += i
    i += 1
now = count - i + 1
nowi = i - 1
if nowi%2 == 1:
    j = nowi
    while j:
        now += 1
        if now == n:
            print(j, nowi + 1 - j, sep="/")
        j -= 1
else:
    j = 1
    while j <= nowi:
        now += 1
        if now == n:
            print(j, nowi + 1 - j, sep="/")
        j += 1