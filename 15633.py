n=int(input())
sqrtn = n**0.5
i = 1
r = 0
while i<=sqrtn:
    if not n%i:
        r+=i+n//i if i!=n//i else i
    i+=1
print(r*5-24)