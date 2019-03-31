m,n=0,0
for i in range(10):
    a,b=map(int,input().split())
    n=n-a+b
    m=m if m>n else n
print(m)