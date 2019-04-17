input()
n=[0]+list(map(int,input().split()))
sum=[n[0]]
for i in range(1,len(n)):sum.append(max(sum[i-1]+n[i], n[i]))
print(max(sum[1:]))