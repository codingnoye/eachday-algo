n = int(input())
import math
for m in range(n):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())
    dis = math.sqrt((x2-x1)*(x2-x1) + (y2-y1)*(y2-y1))
    if dis == 0:
        if r1 == r2:
            print('-1')
        else:
            print('0')
    elif dis == r1 + r2:
        print('1')
    elif dis > r1 + r2:
        print('0')
    elif (dis + r1 == r2) or (dis + r2 == r1): 
        print('1')
    elif (dis + min(r1, r2) < max(r1,r2)):
        print('0')
    else:
        print('2')