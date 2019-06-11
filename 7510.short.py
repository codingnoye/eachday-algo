for i in range(int(input())):
 print(('\n'if i else'')+'Scenario #%d:'%(i+1));print('no'if eval('**2-'.join(map(str,sorted(map(int,input().split()))[::-1]))+'**2')else'yes')