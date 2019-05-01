for i in range(int(input())):
    f=0
    for c in input():
        f+=1 if c=="(" else -1
        if f<0:
            f=1
            break
    print('NO'if f else 'YES')