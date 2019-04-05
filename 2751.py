import sys
l=[]
for i in range(int(sys.stdin.readline())):
    l.append(int(sys.stdin.readline()))
print(*sorted(l),sep="\n")