input()
a=sorted(map(int,input().split()))
print(sum([a[i]*(len(a)-i)for i in range(len(a))]))