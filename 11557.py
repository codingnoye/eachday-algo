for i in range(int(input())):
    high = 0
    highschool = 0 #lol
    for j in range(int(input())):
        school, amount = input().split()
        if int(amount)>high:
            highschool = school
            high = int(amount)
    print(highschool)
