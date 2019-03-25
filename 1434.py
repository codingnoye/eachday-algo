input()

boxes = list(map(int, input().split()))
books = list(map(int, input().split()))

filled = 0
box = boxes.pop(0)
book = books.pop(0)

dumped = 0
filled = 0
flag = 2
while flag > 0:
    if flag == 1:
        flag = 0

    if (filled + book > box) or (flag == 0):
        dumped += box - filled
        filled = 0
        if flag == 2:
            if len(boxes) == 0:
                flag = 1
            else:
                box = boxes.pop(0)
    else:
        filled += book
        if len(books) > 0:
            book = books.pop(0)
        else:
            flag = 1
for i in boxes:
    dumped += i
print(dumped)