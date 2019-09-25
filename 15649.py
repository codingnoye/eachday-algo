import itertools
n, m = map(int, input().split())
print(*map(lambda x:' '.join(map(str, x)), itertools.permutations(range(1, n+1), m)), sep='\n')