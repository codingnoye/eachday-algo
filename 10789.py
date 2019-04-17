s=[''for i in range(75)]
for i in range(5):
    n=input()
    for j in range(len(n)):
        s[j*5+i]=n[j]
print(''.join(s))