trys = int(input())
for t in range(trys):
    n = int(input())
    field = []
    for i in range(n):
        field.append(list(map(int, input().replace("#", '4')))) # 4: 모름 5: 지뢰 아님 6: 지뢰

    if n == 1 or n == 2:
        print('0')
        continue
    elif n == 3:
        if field[0][0] == 0:
            print('0')
            continue
        else:
            print('1')
            continue

    count = (n-4)**2

    field[1][1] = field[0][0] + 5
    field[1][n-2] = field[0][n-1] + 5
    field[n-2][1] = field[n-1][0] + 5
    field[n-2][n-2] = field[n-1][n-1] + 5
    count += [field[1][1], field[1][n-2], field[n-2][1], field[n-2][n-2]].count(6)

    def check (x, y):
        global count
        near = field[x][y]
        unknown = 0
        mine = 0
        for i in range(3):
            if x == 0:
                now = field[1][y-1 + i]
            elif x == n-1:
                now = field[n-2][y-1 + i]
            elif y == 0:
                now = field[x-1 + i][1]
            elif y == n-1:
                now = field[x-1 + i][n-2]

            if now == 4:
                unknown += 1
            elif now == 6:
                mine += 1
        if near == unknown + mine:
            for i in range(3):
                if x == 0:
                    lx = 1
                    ly = y-1 + i
                elif x == n-1:
                    lx = n-2
                    ly = y-1 + i
                elif y == 0:
                    lx = x-1 + i
                    ly = 1
                else:
                    lx = x-1 + i
                    ly = n-2
                if field[lx][ly] == 4:
                    field[lx][ly] = 6
                    count += 1
        elif near == mine:
            for i in range(3):
                if x == 0:
                    lx = 1
                    ly = y-1 + i
                elif x == n-1:
                    lx = n-2
                    ly = y-1 + i
                elif y == 0:
                    lx = x-1 + i
                    ly = 1
                else:
                    lx = x-1 + i
                    ly = n-2
                if field[lx][ly] == 4:
                    field[lx][ly] = 5

    for i in range(1, n-1):
        check(0, i)
        check(i, 0)
        check(n-1, i)
        check(i, n-1)

    print(count)