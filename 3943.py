import sys
dp = {}
def max(a,b):
    return a if a>b else b
def call(now):
    global dp
    if now == 1:
        return 1
    if now not in dp:
        if now%2:
            dp[now] = max(now, call(now*3+1))
        else:
            dp[now] = max(now, call(now//2))
    return dp[now]
for _ in range(int(input())):
    sys.stdout.write(str(call(int(sys.stdin.readline())))+'\n')