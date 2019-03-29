import math
a, b = map(int, input().split(":"))
i = min(min(a, b), int(math.sqrt(max(a, b))))
while i > 1:
    if a % i == 0 and b % i == 0:
        a //= i
        b //= i
    i -= 1
print("{}:{}".format(a, b))