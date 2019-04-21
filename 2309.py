n=list(eval('int(input()),'*9));t=sum(n)-100
for i in range(8):
    for j in range(i+1,9):
        if n[i]+n[j]==t:
            print(*sorted(n[0:i]+n[i+1:j]+n[j+1:]),sep="\n")
            exit(0)