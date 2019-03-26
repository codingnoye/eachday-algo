n,x=map(int,input().split())
print(' '.join(map(str, filter(lambda t:t<x,list(map(int,input().split()))))))