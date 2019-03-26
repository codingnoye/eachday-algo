while True:
    n = int(input())
    if n == 0:
        break
    count = 0
    for i in range(n+1, 2*n+1):
        if i==2:
            count += 1
            continue
        prime = True
        j = 1
        while j*j <= i:
            if i%j == 0:
                prime = False
            j+=1
        if prime: count += 1
    print(count)