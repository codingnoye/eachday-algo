a=eval(input().replace(' ','*'))
print(*map(lambda x:int(x)-a,input().split()))