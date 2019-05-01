import math
n,r=map(int,input().split())
print(math.factorial(n)//(math.factorial(r)*math.factorial(n-r)))