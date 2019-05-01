import math
f=str(math.factorial(int(input())))
for i in range(len(f)):
    if f[-1-i]!='0':
        print(f[-1-i])
        break