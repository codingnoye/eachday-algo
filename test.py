year = int(input("input an year:"))

month = int(input("input a month:"))

day = int(input("input a day:"))

result = 0

for year_specific in range(1, year):

    result = result + 365
    if year_specific % 400 == 0 and month >= 3:
        result = result + 1
    elif year_specific % 100 ==0:
        result = result + 0
    elif year_specific % 4 == 0 and month >= 3:
        result = result + 1
    else:
        result = result + 0

for month_sp in range(1, month):
    if  month_sp == 5 or month_sp == 7 or month_sp ==10 or month_sp ==12:
        result = result + 30
    if month_sp == 3:
        result = result + 28
    if month_sp == 1:
        result = result + 0
    else:
        result = result + 31

result = result + day

if result % 7 == 1:
    print("월요일입니당")
if result % 7 == 2:
    print("화요일입니당")
if result % 7 == 3:
    print("수요일입나당")
if result % 7 == 4:
    print("목요일입니당")
if result % 7 == 5:
    print("금요일입니당")
if result % 7 == 6:
    print("토요일입니당")
if result % 7 == 0:
    print("일요일입니당")