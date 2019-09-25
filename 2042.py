import sys

def safeSum(a, b):
    if b == None: return a
    return a + b

class Node:
    def __init__(self, left, right, parent=None, index = None, val = None):
        self.parent = parent
        if left == None:
            self.sum = val
            self.start = index
            self.end = index
            self.left = None
            self.right = None
            return
        self.left = left
        self.right = right
        if right == None:
            self.sum = left.sum
        else:
            self.sum = left.sum + right.sum
        self.start = self.left.start
        self.end = self.right.end if self.right != None else self.left.end
    
    def trace(self, start, end):
        if self.start >= start and self.end <= end:
            return self.sum
        if self.right == None:
            return self.left.trace(start, end)
        else:
            now = 0
            if self.left.end >= start:
                now += self.left.trace(start, end)
            if self.right.start <= end:
                now += self.right.trace(start, end)
            return now
    
    def findNode(self, index):
        if self.start == self.end:
            if self.left != None:
                return self.left.findNode(index)
            return self
        if self.right == None:
            return self.left.findNode(index)
        if index <= self.left.end:
            return self.left.findNode(index)
        else:
            return self.right.findNode(index)

    def update(self):
        if self.right == None:
            if self.left != None:
                self.sum = self.left.sum
        else:
            self.sum = self.left.sum + self.right.sum
        if self.parent != None:
            self.parent.update()

def build(beforeNodes):
    newNodes = []
    nowNode = []
    for node in beforeNodes:
        nowNode.append(node)
        if len(nowNode) == 2:
            newNode = Node(nowNode[0], nowNode[1])
            nowNode[0].parent = newNode
            nowNode[1].parent = newNode
            newNodes.append(newNode)
            nowNode = []
    if len(nowNode) == 1:
        newNode = Node(nowNode[0], None)
        nowNode[0].parent = newNode
        newNodes.append(newNode)
    return newNodes

n, m, k= map(int, input().split())
nodes = []

for i in range(n):
    nodes.append(Node(None, None, index = i, val = int(sys.stdin.readline())))

while len(nodes) > 1:
    nodes = build(nodes)

for i in range(m+k):
    c, s, e = map(int, sys.stdin.readline().split())
    if c == 1:
        node = nodes[0].findNode(s-1)
        node.sum = e
        node.update()
    else:
        print(nodes[0].trace(s-1, e-1))