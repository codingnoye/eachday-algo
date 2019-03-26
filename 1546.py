input()
l=list(map(int, input().split()))
print(sum(map(lambda x:x/max(l)*100,l))/len(l))