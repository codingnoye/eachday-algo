n = int(input())
tri = ["  *  ", " * * ", "*****"]
oldi=0
i=3
while i<n:
    addtri = []
    for j in tri:
        addtri.append(j+' '+j)
    tri = list(map(lambda x:" "*i+x+" "*i, tri))
    tri  += addtri
    i*=2

for j in tri:
    print(j)
