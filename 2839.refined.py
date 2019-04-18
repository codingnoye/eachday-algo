n = int(input())
mod5 = n % 5
div5 = n // 5
if mod5 == 0:
    print(div5)
elif mod5 == 1:
    if div5>=1:
        print(div5+1)
    else:
        print(-1)
elif mod5 == 2:
    if div5>=2:
        print(div5+2)
    else:
        print(-1)
elif mod5 == 3:
    print(div5+1)
else:
    if div5 >= 1:
        print(div5+2)
    else:
        print(-1)