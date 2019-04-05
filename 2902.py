flag = False
s = '-'+input()
r = ""
for c in s:
    if flag:
        r += c
        flag = False
    if c == '-':
        flag = True
print(r)