import math
case = int(input())
for i in range(case):
    d = int(input())
    def f (n):
        sq = math.sqrt(5)
        return round((1/sq) * (math.pow((1+sq)/2, n) - math.pow((1-sq)/2, n)))
    print("{} {}".format(f(d-1), f(d)))