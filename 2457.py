import sys

month = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)
startFlower = -1
startFlowerOpen = 0
flowerEnds = []
flowerNodes = {}

def day(m, d):
    return sum(month[:m])+d

for flowerId in range(int(input())):
    m1, d1, m2, d2 = map(int, sys.stdin.readline().split())
    startDay = max(day(3, 1), day(m1, d1))
    if startDay > day(m2, d2): continue

    endDay = min(day(11, 31), day(m2, d2))
    if endDay < startDay: continue
    if startDay == endDay: continue
    
    flowerEnds.append(endDay)


    if startDay in flowerNodes.keys():
        flowerNodes[startDay].append(flowerId)
    else:
        flowerNodes[startDay] = [flowerId]

nodeList = sorted(flowerNodes.keys())

checkNode = [60]
count = 0
lastEnd = 0
if 60 not in flowerNodes:
    print(0)
    sys.exit(0)
while True:
    maxEnd = -1
    maxs = []
    for node in checkNode:
        nowNode = flowerNodes[node]
        nowMax = max(map(lambda x:flowerEnds[x], nowNode))
        maxs.append(nowMax)
    count += 1
    maxEnd = max(maxEnd, *maxs)
    if maxEnd == -1:
        print(0)
        break
    if maxEnd == day(11, 31):
        print(count)
        break
    checkNode = []
    for node in nodeList:
        if node <= maxEnd and lastEnd < node:
            checkNode.append(node)
    lastEnd = maxEnd
    if len(checkNode) == 0:
        print(0)
        break