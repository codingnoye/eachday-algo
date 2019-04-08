print('n e')
print('- -----------')
counter=2.5
bunmo = 6
print(0, 1)
print(1, 2)
print(2, 2.5)
for i in range(3, 10):
    counter += 1/bunmo
    bunmo*=(i+1)
    print(i, round(counter*1000000000)/1000000000)