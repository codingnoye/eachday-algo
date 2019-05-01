n=int(input())
dp=[1,3]
if n<2:
    print(dp[n-1])
    exit(0)
for i in range(2,n):
    dp.append(dp[i-1]+2*dp[i-2])
print(dp[n-1]%10007)