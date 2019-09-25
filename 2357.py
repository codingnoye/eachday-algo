import sys

nodes = []

def safeMin(a, b):
    if b == None: return a
    return a if a<=b else b

def safeMax(a, b):
    if b == None: return a
    return a if a>=b else b

class Node:
    def __init__(self, left, right, index = None, val = None):
        if left == None:
            self.min = val
            self.max = val
            self.start = index
            self.end = index
            self.left = None
            self.right = None
            return
        self.left = left
        self.right = right
        if right == None:
            self.min = left.min
            self.max = left.max
        else:
            self.min = safeMin(left.min, right.min)
            self.max = safeMax(left.max, right.max)
        self.start = self.left.start
        self.end = self.right.end if self.right != None else self.left.end
    
    def traceMin(self, start, end):
        #print(f'self.start {self.start} / self.end {self.end} / start {start} / end {end}')
        if self.start >= start and self.end <= end:
            return self.min
        if self.right == None:
            return self.left.traceMin(start, end)
        else:
            now = []
            if self.left.end >= start:
                now.append(self.left.traceMin(start, end))
            if self.right.start <= end:
                now.append(self.right.traceMin(start, end))

            return min(now)
    
    def traceMax(self, start, end):
        #print(f'self.start {self.start} / self.end {self.end} / start {start} / end {end}')
        if self.start >= start and self.end <= end:
            return self.max
        if self.right == None:
            return self.left.traceMax(start, end)
        else:
            now = []
            if self.left.end >= start:
                now.append(self.left.traceMax(start, end))
            if self.right.start <= end:
                now.append(self.right.traceMax(start, end))

            return max(now)

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
    print(rootNode.traceMin(s-1, e-1), rootNode.traceMax(s-1, e-1))