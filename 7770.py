n = int(input())
i = 0
block = 1
while n>=0:
    block += 4*i
    n -= block
    i += 1
print(i-1)