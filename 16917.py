a,b,c,x,y = map(int,input().split())
ab = 2*c
chi = sorted([[x, a],[y, b]], key=lambda x:x[0])
price = 0
if ab<a+b:
    price += ab*chi[0][0]
    price += min(ab*(chi[1][0]-chi[0][0]), chi[1][1]*(chi[1][0]-chi[0][0]))
else:
    if chi[0][1]>=ab:
        price += ab*chi[0][0]
        price += max(chi[1][0]-chi[0][0], 0)*chi[1][1]
    elif chi[1][1]>=ab:
        price += ab*chi[1][0]
        price += max(chi[0][0]-chi[1][0], 0)*chi[0][1]
    else:
        price += chi[0][0]*chi[0][1]
        price += chi[1][0]*chi[1][1]
print(price)