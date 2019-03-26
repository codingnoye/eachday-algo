s = input().upper()
counter = {}
for c in s:
    counter[c] = counter[c]+1 if c in counter else 1
isMany = False
m = 0
mkey = -1
for i in counter.items():
    if m < i[1]:
        m = i[1]
        mkey = i[0]
        isMany = False
    elif m == i[1]:
        isMany = True
print('?' if isMany else mkey)