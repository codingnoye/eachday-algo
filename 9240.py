maxlength=0
minradius=0
points=[]
for i in range(int(input())):
    x,y=map(int,input().split())
    if x*x+y*y<=minradius: continue
    points.append((x,y))
    for point in points:
        px,py=point[0],point[1]
        if (px-x)*(px-x)+(py-y)*(py-y)>maxlength:
            maxlength=(px-x)*(px-x)+(py-y)*(py-y)
            minradius = min(px*px+py*py, x*x+y*y)
print(maxlength**0.5)