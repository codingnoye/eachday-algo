import sys
cases = int(sys.stdin.readline())
li = [int(sys.stdin.readline())]
for i in range(cases-1):
    n = int(sys.stdin.readline())
    start = 0
    lenli = len(li)
    end = lenli
    while True:
        print(li)
        now = int(end/2)
        print(now, li[now], n)
        if li[now]<=n:
            if now==lenli-1:
                li.append(n)
                break
            if li[now+1]>=n:
                li.insert(now, n)
                break
            now = int(now+end/2)
        else:
            if now==0: li.insert(0, n)
            now = int(now/2)
print('\n'.join(map(str,li)))