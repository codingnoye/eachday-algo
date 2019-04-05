day = ['Wednesday','Thursday','Friday','Saturday','Sunday','Monday','Tuesday']
monthday = [31,28,31,30,31,30,31,31,30,31,30,31]
date = 0
d, m = map(int, input().split())
for i in range(m-1):
    date += monthday[i]
print(day[(date+d)%7])