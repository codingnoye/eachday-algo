remember = [[0 for j in range(14)] for i in range(15)]
remember[0] = [1,2,3,4,5,6,7,8,9,10,11,12,13,14]
for i in range(1, 15):
    remember[i][0] = 1
    for j in range(1, 14):
        remember[i][j] = remember[i-1][j] + remember[i][j-1]
for i in range(int(input())):
    print(remember[int(input())][int(input())-1])