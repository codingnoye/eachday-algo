class Stack:
    _stack = []
    def push(self, value):
        self._stack.append(value)
    def size(self):
        return len(self._stack)
    def pop(self):
        if self.size() != 0:
            return self._stack.pop()
        else:
            return -1
    def empty(self):
        if self.size() == 0:
            return 1
        else:
            return 0
    def top(self):
        if self.size() != 0:
            return self._stack[-1]
        else:
            return -1

stack = Stack()
n = int(input())
for i in range(n):
    op = input().split()
    if op[0]=="push":
        stack.push(int(op[1]))
    elif op[0]=="pop":
        print(stack.pop())
    elif op[0]=="empty":
        print(stack.empty())
    elif op[0]=="top":
        print(stack.top())
    else:
        print(stack.size())