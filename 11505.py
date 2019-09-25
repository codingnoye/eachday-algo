import sys

def build(tree, indTree, now):
    nowtree = tree[now]
    newtree = []
    nowIndTree = indTree[now]
    newIndTree = []
    for i in range(0, len(nowtree), 2):
        newtree.append(nowtree[i] * nowtree[i+1])
        newIndTree.append(nowIndTree[i])
    tree.append(newtree)
    indTree.append(newIndTree)
    if len(newtree) > 1:
        build(tree, indTree, now+1)
        
def change(tree, n, newval):
    tree[0][n] = newval
    for i in range(1, len(tree)):
        tree[i][n//(2**i)] = tree[i-1][n//(2**i)*2] * tree[i-1][n//2**i*2+1]

def trace(tree, s, e, d, now):
    #print(s, e, d , now)
    if d==0:
        if s==now or e==now:
            #print(4)
            return tree[d][now]
        #print(5)
        return 1
    start, end = indTree[d-1][now*2], indTree[d-1][now*2+1]+1
    left, right = tree[d-1][now*2], tree[d-1][now*2+1]+1
    if start >= s and end <= e:
        #print(1)
        return tree[d][now]
    if start < s and end > e:
        #print(2)
        return 1
    #print(3)
    return trace(tree, s, e, d-1, now*2) * trace(tree, s, e, d-1, now*2+1)


n, m, k = map(int, input().split())
now = []
indNow = []
for i in range(n):
    now.append(int(sys.stdin.readline()))
    indNow.append(i)

floor = 1
while floor < len(now):
    floor *= 2
now.extend([1] * (floor - len(now)))
indNow.extend([-1] * (floor - len(indNow)))
tree = [now]
indTree = [indNow]

build(tree, indTree, 0)


for _ in range(m+k):
    #print(tree)
    #print(indTree)
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        change(tree, inp[1]-1, inp[2])
    else:
        print(trace(tree, inp[1]-1, inp[2], len(tree)-1, 0)%1000000007)