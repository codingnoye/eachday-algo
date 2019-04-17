e, s, m = map(int, input().split())
a, b, c = 0, 0, 0
counter = 1
while True:
    if (a+1==e) and (b+1==s) and (c+1==m):
        print(counter)
        break
    a, b, c = (a+1)%15, (b+1)%28, (c+1)%19
    counter += 1