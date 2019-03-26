n = int(input())
queue = [(n, 0)]
while True:
    item = queue.pop(0)
    if item[0] == 1:
        print(item[1])
        break
    if item[0] % 3 == 0:
        queue.append((item[0]//3, item[1]+1))
    if item[0] % 2 == 0:
        queue.append((item[0]//2, item[1]+1))
    queue.append((item[0]-1, item[1]+1))