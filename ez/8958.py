import re
n=int(input())
for i in range(n):
    print(sum(map(lambda x: ((len(x)*len(x))+len(x))//2,re.sub('X+', ' ', input()).split())))