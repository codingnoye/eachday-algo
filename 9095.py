d=lambda n:0 if n<0 else d(n-1)+d(n-2)+d(n-3)if n>0 else 1
print(*eval('d(int(input())),'*int(input())))