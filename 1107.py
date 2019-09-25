s = input()
n = int(s)
input()
bset = set(map(int, input().split()))

def checker(n):
    res = []
    res.append(n%10)
    if n>=10:
        res += checker(n//10)
    return res
i = 0
res = 0
while True:
    if len(set(checker(n-i)) & bset) == 0:
        res = n-i
        break
    if len(set(checker(n+i)) & bset) == 0:
        res = n+i
        break
    i+=1
print(min(abs(n-res) + len(str(res)), n-100))