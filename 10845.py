queue = []
for i in range(int(input())):
    now = input().split()
    if now[0] == "push":
        queue.append(now[1])
    elif now[0] == "pop":
        print(queue.pop(0) if len(queue) else -1)
    elif now[0] == "size":
        print(len(queue))
    elif now[0] == "empty":
        print(0 if len(queue) else 1)
    elif now[0] == "front":
        print(queue[0] if len(queue) else -1)
    elif now[0] == "back":
        print(queue[len(queue)-1] if len(queue) else -1)