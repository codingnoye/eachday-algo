n=int(input())
for i in range(n-1):print(' '*i+'*'*(2*n-2*i-1))
for i in range(n-1,-1,-1):print(' '*i+'*'*(2*n-2*i-1))