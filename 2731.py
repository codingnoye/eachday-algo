for c in range(int(input())):
    s = input()
    n = int(s)
    f = 0
    if s[-1]=='1':   f = 1
    elif s[-1]=='3': f = 7
    elif s[-1]=='7': f = 3
    else:            f = 9

    for ii in range(2, len(s)+1):
        for i in range(1, 10):
            now = i*(10**(ii-1)) + f
            if str(now**3)[-ii:] == s[-ii:]:
                f = now
                break
    print(f)