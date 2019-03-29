n = int(input())
l = []
for i in range(n):
    age, name = input().split()
    l.append((int(age), name))
l.sort(key = lambda x:x[0])
for item in l:
    print('{} {}'.format(item[0], item[1]))