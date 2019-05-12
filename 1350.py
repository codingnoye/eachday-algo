input()
l,c=map(int,input().split()),int(input())
print(sum(map(lambda x:(x+c-1)//c,l))*c)