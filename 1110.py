n = input()
n = '0'+n if len(n) < 2 else n
m = n
count = 0
while True:
    count += 1
    m = m[1] + str(int(m[0]) + int(m[1]))[-1]
    m = '0'+m if len(m) < 2 else m
    if m == n:
        print(count)
        break
