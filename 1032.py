s = []
res = []
for c in range(int(input())):
    s.append(input())
for i in range(len(s[0])):
    same = True
    before = 0
    before = s[0][i]
    for j in s:
        if j[i] != before:
            same = False
    if same:
        res.append(j[i])
    else:
        res.append("?")
print(''.join(res))