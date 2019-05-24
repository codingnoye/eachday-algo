a,b,c=0,0,100
for i in [int(input())for _ in range(10)]:
 a+=i;d=abs(a-100)
 if c>=d:b,c=a,d
print(b)