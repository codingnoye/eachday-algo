old = 0
count = 1
for i in range(int(input())-1):
    old, count = count, old+count
print(count)