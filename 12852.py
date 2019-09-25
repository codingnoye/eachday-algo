n = int(input())
queue = [(n, 0)]
did = []
log = []
while True:
    item = queue.pop(0)
    if item[0] == 1:
        print(item[1])
        break
    if item[0] % 3 == 0:
        div3 = item[0]//3
        if (div3, item[1]+1) in did:
            continue
        else:
            queue.append((div3, item[1]+1))
            did.append((div3, item[1]+1))
    if item[0] % 2 == 0:
        div2 = item[0]//2
        if div2 in did:
            continue
        else:
            queue.append((div2, item[1]+1))
            did.append(div2)
    if not ((item[0]-1, item[1]+1) in did):
        queue.append((item[0]-1, item[1]+1))