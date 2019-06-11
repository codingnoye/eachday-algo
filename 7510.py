for i in range(int(input())):
 l=sorted([i*i for i in map(int,input().split())])
 print('Scenario #%s:\n%s\n'%(i+1,['no','yes'][l[0]+l[1]==l[2]]))