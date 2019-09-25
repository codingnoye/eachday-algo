import sys
sys.setrecursionlimit(10**6)
costs = []
for _ in range(int(input())):
    costs.append(list(map(int, sys.stdin.readline().split())))
memo = [[-1,-1,-1] for _ in range(len(costs))]
def trace(index, now):
    #print(index, now)
    global costs
    if index==len(costs):
        return 0
    if memo[index][now] == -1:
        memo[index][now] = min(
            [trace(index+1, i) for i in ((1, 2), (0, 2), (0, 1))[now]]
        )
    return costs[index][now] + memo[index][now]
print(
    min(trace(0, 0), trace(0, 1), trace(0, 2))
    )