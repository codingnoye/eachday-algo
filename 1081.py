partsum = [0, 1, 3, 6, 10, 15, 21, 28, 36, 45]
def jari(a, l):
    global partsum
    if l==0:
        return partsum[a]
    res = 10**l*partsum[a-1] + (10**(l-1)*a*45)*l + a
    return res
#s,e = input().split()
#s = str(int(s)-1)
s=input()
total = 0
#total2 = 0
#for c in range(len(e)):
#    total+=jari(int(e[c]),len(e)-c-1)
for c in range(len(s)):
    total+=jari(int(s[c]),len(s)-c-1)
print(total)
'''
0~9 = 0~9 = 45
0~19 = 0~1*10 + 0~9*2 = 100
0~29 = 0~2*10 + 0~9*3 = 165
0~99 = 0~9*10 + 0~9*10 = 900
0~199 = 0~1*100 + 0~9*20 + 0~9*20 = 1900
0~299 = 0~2*100 + 0~9*30 + 0~9*30 = 3000
0~999 = 0~9*100 + 0~9*100 + 0~9*100
0~1999 = 0~1*1000 + 0~9*200 + 0~9*200 + 0~9*200
0~9999 = 0~9*4000

492834
->
400000 + 90000 + 2000 + 800 + 30 + 4
399999 + 89999 + 1999 + 799 + 29 + 4
'''