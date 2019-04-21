li = []
for i in range(int(input())):
    li.append(int(input()))
last = len(li)-1
dp = [0]*len(li)
def call(now):
    global li, dp
    if now<=0:
        return max(li[now+1]+call(now+2), li[now+1]+li[now+2]+call(now+3))
    if now >= last:
        return -3000000
    if now+1 == last:
        return li[last]
    if now+2 == last:
        return li[last-1]+li[last]
    if dp[now]:
        return dp[now]
    dp[now] = max(li[now+1]+call(now+2), li[now+1]+li[now+2]+call(now+3))
    return dp[now]
print(max(call(-1), call(0)))