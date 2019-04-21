l=int(input());n=list(map(int,input().split()))
ps,li=[0],[]
for i in range(l):
    ps+=[n[i]*(i+1)]
    li+=[str(n[i]*(i+1)-ps[i])]
print(' '.join(li))