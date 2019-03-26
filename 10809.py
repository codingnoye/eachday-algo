s = input()
res = []
for c in 'abcdefghijklmnopqrstuvwxyz':
    res.append(str(s.find(c)))
print(' '.join(res))