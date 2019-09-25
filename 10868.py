import sys

nodes = []

def safeMin(a, b):
    if b == None: return a
    return a if a<=b else b

class Node:
    def __init__(self, left, right, index = None, val = None):
        if left == None:
            self.min = val
            self.start = index
            self.end = index
            self.left = None
            self.right = None
            return
        self.left = left
        self.right = right
        if right == None: self.min = left.min
        else: self.min = safeMin(left.min, right.min)
        self.start = self.left.start
        self.end = self.right.end if self.right != None else self.left.end
    
    def trace(self, start, end):
        #print(f'self.start {self.start} / self.end {self.end} / start {start} / end {end}')
        if self.start >= start and self.end <= end:
            return self.min
        if self.right == None:
            return self.left.trace(start, end)
        else:
            now = []
            if self.left.end >= start:
                now.append(self.left.trace(start, end))
            if self.right.start <= end:
                now.append(self.right.trace(start, end))

            return min(now)

def build(beforeNodes):
    newNodes = []
    nowNode = []
    for node in beforeNodes:
        nowNode.append(node)
        if len(nowNode) == 2:
            newNodes.append(Node(nowNode[0], nowNode[1]))
            nowNode = []
    if len(nowNode) == 1:
        newNodes.append(Node(nowNode[0], None))
    return newNodes

n, m = map(int, input().split())
node = []

for i in range(n):
    nodes.append(Node(None, None, index = i, val = int(sys.stdin.readline())))

while len(nodes) > 1:
    nodes = build(nodes)
rootNode = nodes[0]

for i in range(m):
    s, e = map(int, sys.stdin.readline().split())
    print(rootNode.trace(s-1, e-1))