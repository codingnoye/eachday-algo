n = int(input())

if n % 2 != 0:
    print(0)
    exit(0)

def call (i) :
    if i==n:
        return 1
    res =  call (i+2)
    for j in range(i+2, n+1, 2):
        res += 2 * call (j)
    return res

print(call(0))
