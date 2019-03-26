l = []
for i in range(5):
    j = int(input())
    l.append(40 if j<40 else j)
print(sum(l)//len(l))