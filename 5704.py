while 1:
    s=input()
    if s=="*":break
    f=list('abcdefghijklmnopqrstuvwxyz')
    for c in s:
        if c in f:f.remove(c)
    print('N'if len(f)else 'Y')