inp = int(input())
for i in range(1, inp):
    print((inp-i)*' '+'*'*1+' '*(2*i-3)+('*'if i-1 else''))
print('*'*(inp*2-1))