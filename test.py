n=int(input("임의의 정수 n을 지정하세요/ n ="))

a=[]
b=[]
for i in range(2,n+1):
    a.append(i)
    b.append(i)

for i in range(1,len(a)):
    for j in range(1,len(a)):
        if a[i]!=j:
            if (a[i]%j==0):
                b.remove(b[i])