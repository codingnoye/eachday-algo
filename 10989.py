import sys
li = [0 for i in range(10001)]
for i in range(int(input())):
    li[int(sys.stdin.readline())]+=1
for i in range(len(li)):
    sys.stdout.write((str(i)+'\n')*li[i])