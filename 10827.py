a, b = input().split()
b = int(b)
sosulen = len(a)-(a.find('.')+1)
inta = int(float(a) * (10**sosulen))
res = str(inta**b)
if len(res)-sosulen*b<0:
    res = '0'*(1-(len(res)-sosulen*b))+res
dotindex = len(res)-sosulen*b
front = res[:dotindex]
end = res[dotindex:]
if int(end) == 0:
    print(front)
else:
    print(front+'.'+end)