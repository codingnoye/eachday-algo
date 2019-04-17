while 1:
    s,n=input(),0
    if s=='#':break
    for c in set(s.upper()):
        o=ord(c)
        if 64<o and o<91:n+=1
    print(n)