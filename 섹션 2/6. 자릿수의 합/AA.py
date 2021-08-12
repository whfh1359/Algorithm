import sys
sys.stdin = open("in1.txt", "rt")
n = int(input())
a = list(map(int, input().split()))
max = -21470000
def digit_sum(x):
    sum = 0
    while x> 0:
        sum += x%10
        x = x//10
    return sum

for idx, x in enumerate(a):
    tot = digit_sum(x)
    if max < tot:
        max = tot
        num = idx
print(a[num])
