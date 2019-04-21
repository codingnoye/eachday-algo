o=-1000000
for i in map(int,input().split()):
    if i<o:
        print('Bad')
        break
    o=i
else:print('Good')