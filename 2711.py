for i in range(int(input())):
    w, s = input().split()
    print(s[0:int(w)-1]+s[int(w):])
