x,y=[],[]
for i in range(3):
    n=input().split()
    x.append(n[0])
    y.append(n[1])
x.sort()
y.sort()
print(x[2]if x[1]==x[0]else x[0],y[2]if y[1]==y[0]else y[0])