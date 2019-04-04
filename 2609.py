n,m=map(int,input().split())
def gcd(a,b):return gcd(b,a%b)if b else a
print(gcd(n, m));print(n*m//gcd(n,m))