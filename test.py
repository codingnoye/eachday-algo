a = []
total = 0
for i in range(9):
    b = int(input())
    a.append(b)
for i in range(9):
    total += a[i]
print(total, sum(a))
for i in range(9):
  for j in range(i+1,9):
      if a[i]+a[j] == (total-100) :
          print(a[i], a[j])
          del a[i], a[j]
          print(a)
          a.sort()
          for k in range(7):
              print(a[k])
          exit()