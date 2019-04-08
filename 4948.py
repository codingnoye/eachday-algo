era = [2]
maxchecked = 2
while True:
    n = int(input())
    if n==0:
        break
    elif 2*n>maxchecked:
        for i in range(maxchecked+1, 2*n+1):
            issosu = True
            for sosu in era:
                if sosu*sosu>i:break
                if i%sosu==0:
                    issosu = False
            if issosu:
                era.append(i)
            maxchecked = i
    count = 0
    for i in era:
        if i>n*2: break
        if i>n: count += 1
    print(count)