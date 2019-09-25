import sys

def build(base, now):
    global tree, indTree
    tree = [tree[i] * tree[i*1] for i in range(base, base+now, 2)] + tree
    if now != 1:
        build(base+now, now//2)    

def trace(index, start, end, left, right):
    global tree, indTree
    if start > right or left < end:
        return 1
    if start <= left and right <= end:
        return tree[index]
    mid = (left + right)//2
    return trace(index*2+1, start, end, left, mid) * trace(index*2+2, start, end, mid+1, right)

def update(find):
    
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
    inp = list(map(int, sys.stdin.readline().split()))
    if inp[0] == 1:
        change(tree, inp[1]-1, inp[2])
    else:
        print(trace(tree, inp[1]-1, inp[2], len(tree)-1, 0)%1000000007)