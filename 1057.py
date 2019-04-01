n,a,b=map(int,input().split())
oldarr = [0 for i in range(1, n+1)]
oldarr[a-1], oldarr[b-1] = 1, 1
count = 0
while True:
    newarr = []
    count += 1
    for i in range(0, len(oldarr), 2):
        if len(oldarr)-1 == i:
            newarr.append(oldarr[i])
        elif oldarr[i] and oldarr[i+1]:
            print(count)
            exit(0)
        else:
            newarr.append(1 if oldarr[i] or oldarr[i+1] else 0)
    oldarr = newarr
