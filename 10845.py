import sys
queue = []
for i in range(int(input())):
    now = sys.stdin.readline()[:-1]
    act = now[:4]
    if act == "push":
        queue.append(now[5:])
    elif act == "pop":
        print(queue.pop(0) if len(queue) else -1)
    elif act == "size":
        print(len(queue))
    elif act == "empt":
        print(0 if len(queue) else 1)
    elif act == "fron":
        print(queue[0] if len(queue) else -1)
    elif act == "back":
        print(queue[len(queue)-1] if len(queue) else -1)