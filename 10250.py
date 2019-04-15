for c in range(int(input())):
    h,w,n=map(int,input().split())
    x,y=(n-1)%h,(n-1)//h+1
    print(str(x+1)+str(y if y>9 else'0'+str(y)))