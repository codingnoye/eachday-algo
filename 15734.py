a, b, c = map(int, input().split())
for i in range(c):
    if a<b:
        a+=1
    else:
        b+=1
print(a+b - (a-b if a-b>0 else -(a-b)))