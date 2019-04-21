li = []
for i in range(int(input())):
    li.append(int(input()))
last = len(li)-1
dp = [0]*len(li)
def call(now, score):
    global li, dp
    if now == last:
        return 0
    if now == last-1:
        return score+li[last]
    if now == last-2:
        return score+li[last-1]+li[last]
    if dp[now]:
        return dp[now]
    dp[now] = max(call(now+2, score+li[now+1]), call(now+3, score+li[now+1]+li[now+2]))
    return dp[now]
print(max(call(-1, 0), call(0, 0)))
print(li, dp)