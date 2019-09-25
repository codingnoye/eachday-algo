data = input("입력:")
target = int(input("뭘 원해?"))
numbers = data.split()
numbers = [int(i) for i in numbers]

lower = 0
upper = len(numbers) - 1
idx = -1
while (lower <= upper):
    middle = int((lower+upper)//2)
    if numbers[middle] == target:
        idx = middle
        break
    elif numbers[middle] < target:
        lower = middle + 1
    else:
        upper = middle - 1
if idx == -1:
    print("찾지 못한 숫자:", target)
else:
    print("타겟 %d은 %d번째 있다."%(target, idx))