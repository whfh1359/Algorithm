import sys
sys.stdin = open("in1.txt", "rt")

def Count(state):
    cnt =1
    point = a[0]
    for x in a:
        if x-point >= state:
            cnt += 1
            point = x
    return cnt

n, c = map(int, input().split())
a = []
largest = 0
for i in range(n):
    k = int(input())
    a.append(k)
    largest = max(largest, k)

a.sort()
lt = 1
rt = largest
res = 0

while lt<=rt:
    mid = (lt+rt)//2
    if Count(mid) >= c:
        res = mid
        lt = mid+1
    else:
        rt = mid-1
print(res)

