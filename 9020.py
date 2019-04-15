inp = []
for c in range(int(input())):
    inp.append(int(input()))
sosu = [2]
for i in range(2, max(inp)-1):
    issosu = True
    for s in sosu:
        if i%s == 0:
            issosu = False
            break
    if issosu:
        sosu.append(i)
arcind = []
i=1
j=0
while j<len(sosu):
    arcind.append(j)
    if i>sosu[j]:
        j+=1
    i+=1
for c in inp:
    stop = False
    for s1 in sosu[arcind[int(c/2)]::-1]:
        if stop: break
        for s2 in sosu[arcind[int(c/2)]:]:
            if s1+s2 == c:
                print(s1, s2)
                stop = True
                break