n = int(input())
if n <= 99:
    print(n)
else:
    count = 99
    for i in range(111, n+1):
        now = str(i)
        dif = int(now[1]) - int(now[0])
        for j in range(1, len(now) - 1):
            if dif != int(now[j+1]) - int(now[j]):
                break
            else:
                count += 1
    print(count)
