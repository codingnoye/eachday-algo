n = int(input())
count = 0
for i in range(n):
    used = []
    s = input()
    was = ''
    flag = True
    for c in s:
        if was == c:
            pass
        else:
            if used.count(c) != 0:
                flag = False
                break
            used.append(was)
            was = c
    if flag: count += 1
print(count)