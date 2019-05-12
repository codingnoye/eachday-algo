s = 0
for i in range(1, int(input())+1):
    s+=sum(int(c) for c in str(i))
print(s)