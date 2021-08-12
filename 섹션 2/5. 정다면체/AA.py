import sys
sys.stdin = open("in1.txt", "rt")

n, m = map(int, input().split())
res = tuple()
cnt = [0]*(n+m+2)
for i in range(1,n+1):
    for j in range(1,m+1):
        cnt[i+j] += 1
for i in range(len(cnt)):
    if cnt[i] == max(cnt):
        print(i, end= ' ')
