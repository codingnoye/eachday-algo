import sys
li = list(map(lambda l:eval(l.replace(' ', '+')), sys.stdin.readlines()))
li[0] = li[-1]
sm = 0
for i in range(1, len(li)): sm += abs(li[i]-li[i-1])
print(sm)