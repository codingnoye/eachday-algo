import sys
n, m = map(int, sys.stdin.readline().split())
li = []
dic = {}
for i in range(n):
    name = input()
    li.append(name)
    dic[name] = i+1
for i in range(m):
    inp = sys.stdin.readline()[:-1]
    if inp.isdigit():
        print(li[int(inp)-1])
    else:
        print(dic[inp])