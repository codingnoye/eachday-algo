n = int(input())
for i in range(n):
    li = list(map(int, input().split()[1:]))
    avg = sum(li)/len(li)
    cnt = 0
    for j in range(len(li)):
        if li[j] > avg:
            cnt += 1
    print("{0:0.3f}%".format(cnt/len(li) * 100))
