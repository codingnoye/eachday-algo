s=[1 for i in range(10000)]
for i in range(10000):
    a=str(i+1)
    b=i+1
    for j in a:
        b+=int(j)
    s[b-1 if b<10001 else 1]=0
for i in range(10000):
    if s[i]:
        print(i+1)