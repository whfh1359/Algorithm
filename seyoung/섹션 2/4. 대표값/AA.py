import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
avg = round((sum(a)+0.5)/n)
distMin = 2147000000
for idx, x in enumerate(a):
    tmp = abs(x-avg)
    if tmp < distMin:
        distMin = tmp
        score = x
        res = idx + 1
    elif tmp == distMin:
        if x > score:
            score = x
            res = idx + 1

print(avg, res)
