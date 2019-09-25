import sys
s,p=[],print
for _ in'0'*int(input()):
 i=sys.stdin.readline();k,l=i[0],len(s)
 if i[:2]=='pu':s.append(i[5:-1])
 else:p(s.pop()if l else-1 if k=='p'else l if k=='s'else int(not l)if k=='e'else s[l-1]if l else-1)