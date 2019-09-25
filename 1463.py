n = int(input())
queue = [(n, 0)]
did = []
while True:
    item = queue.pop(0)
    if item[0] == 1:
        print(item[1])
        break
    if (item[0], item[1]+1) in did:
        continue
    if item[0] % 3 == 0:
        div3 = item[0]//3
        queue.append((div3, item[1]+1))
        did.append((div3, item[1]+1))
    if item[0] % 2 == 0:
        div2 = item[0]//2
        queue.append((div2, item[1]+1))
        did.append(div2)
    queue.append((item[0]-1, item[1]+1))