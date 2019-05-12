li = [*map(int, input().split())]
time = (li[0]*3600+li[1]*60+li[2]+int(input()))%(24*3600)
print(time//3600, (time%3600)//60, time%60)