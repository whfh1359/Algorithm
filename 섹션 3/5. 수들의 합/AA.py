import sys
sys.stdin = open("in1.txt", "rt")

n,m = map(int, input().split())
a = list(map(int, input().split()))
tot = a[0] #lt부터 rt 앞까지 부분합
lt = 0
rt = 1
cnt=0

while True:
    if tot < m:
        if rt<n:
            tot += a[rt]
            rt += 1
        else:
            break
    elif tot == m:
        cnt += 1
        tot -= a[lt]
        lt +=1
    else:
        tot -= a[lt]
        lt += 1
print(cnt)
