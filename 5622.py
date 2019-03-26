s = input()
li = []
time = 0
for c in s:
    where = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(c)
    if where <= 2: # ABC
        time += 3
    elif where <= 5: # DEF
        time += 4
    elif where <= 8: # GHI
        time += 5
    elif where <= 11: # JKL
        time += 6
    elif where <= 14: # MNO
        time += 7
    elif where <= 18: # PQRS
        time += 8
    elif where <= 21: # TUV
        time += 9
    else: # WXYZ
        time += 10
print(time)