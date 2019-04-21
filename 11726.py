n = int(input())
dp = [-1 for i in range(1000)]
def backtrack(i):
    global n, dp
    if i>n: return 0
    if i==n: return 1
    if dp[i] == -1: dp[i] = backtrack(i+2) + backtrack(i+1)
    return dp[i]
print(backtrack(0)%10007)