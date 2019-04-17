dic = {}
li = []
for i in range(int(input())):
    now = int(input())
    if now in dic: dic[now] += 1
    else: dic[now] = 1
    li.append(now)
li.sort()
print(round(sum(li)/len(li)))
print(li[len(li)//2])
dic = sorted(dic.items(), key=lambda x:-x[1])
dic = sorted(filter(lambda x: x[1]==dic[0][1], dic), key=lambda x:x[0])
print(dic[1][0] if len(dic)>1 else dic[0][0])
print(li[len(li)-1]-li[0])