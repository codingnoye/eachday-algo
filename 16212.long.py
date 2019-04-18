input()
dic = {}
for i in map(int, input().split()):
    if not (i in dic):
        dic[i] = 0
    dic[i] += 1
dic = sorted(dic.items(), key=lambda x:x[0])
for i in dic:
    print((str(i[0])+" ")*i[1], end="")