a,b=map(int,input().split())
c,d=map(int,input().split())
e,f=a*d+c*b,b*d
def g(a,b):
    while b:temp=a%b;a=b;b=temp
    return abs(a)
h=g(e,f)
print(e//h,f//h)