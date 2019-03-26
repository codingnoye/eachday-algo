x, y = map(int, input().split())
mon = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
days = y
for i in range(x-1):
    days+=mon[i]
day = days % 7
print('SUNMONTUEWEDTHUFRISAT'[day*3:day*3+3])