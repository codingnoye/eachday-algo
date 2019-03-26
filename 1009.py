m = int(input())
for n in range(m):
    a, b = map(int, input().split())
    blist = []
    temp = b
    i = 0
    while (temp > 0):
        if temp&1:
            blist.append(2**i)
        temp = temp >> 1
        i += 1
    # print(blist)
    restotal = 1

    for bi in blist:
        res = a
        i = 1
        while i*2 <= bi:
            res = (res * res) % 10
            i *= 2
            # print(bi, i, res)
        restotal *= res%10

    print((restotal-1)%10+1)