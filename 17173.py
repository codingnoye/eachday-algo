n,m=map(int,input().split())
s={0}
for i in [*map(int,input().split())]:
    for j in range(i,n+1,i):s.add(j)
print(sum(s))