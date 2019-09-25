import sys
sys.setrecursionlimit(10**6)
input()
nums = list(map(lambda item:list(map(int, item.split())), sys.stdin.readlines()))
memo = [[-1] * i for i in range(1, len(nums)+1)]
def trace(index, now):
    global nums, memo
    if index==len(nums):
        return 0
    if memo[index][now] == -1:
        memo[index][now] = max(
            trace(index+1, now), trace(index+1, now+1)
        )
    return nums[index][now] + memo[index][now]
print(trace(0, 0))