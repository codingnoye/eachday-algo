n = int(input())
def call(sugar, b3, b5):
    if sugar == 0:
        print(b3+b5)
        exit(0)
    elif sugar < 0:
        return
    call(sugar-5, b3, b5+1)
    call(sugar-3, b3+1, b5)
call(n, 0, 0)
print(-1)