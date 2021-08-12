import sys
sys.stdin = open("in1.txt", "rt")

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
k = int(input())
for i in range(k):
    row,state,num = map(int, input().split())
    if state == 0:
        for _ in range(num):
            a[row-1].append(a[row-1].pop(0))
    else:
        for _ in range(num):
            a[row-1].insert(0, a[row-1].pop())
res = 0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i<n//2:
        s+=1
        e-=1
    else:
        s-=1
        e+=1
print(res)
