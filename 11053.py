input()
li = [*map(int,input().split())]
dp = [1]*(len(li))
i = len(li)-2
while 0<=i:
    mx=1
    for j in range(i+1, len(li)):
        if li[j] > li[i]:
            mx = max(mx, dp[j]+1)
    dp[i] = mx
    i-=1
print(max(dp))