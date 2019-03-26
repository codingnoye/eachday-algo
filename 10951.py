while True:
    try:
        a=input()
        print(int(a[0])+int(a[2]))
    except EOFError:
        break
