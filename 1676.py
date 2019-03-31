def f(x):return x*f(x-1) if x>1 else 1
a=list(str(f(int(input()))));c=0
for i in list(reversed(a)):
    if i!='0':break
    c+=1
print(c)