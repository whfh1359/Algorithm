#import sys
from collections import deque
#sys.stdin = open("in1.txt", "rt")

n, k = map(int, input().split())
a = list(range(1,n+1))
a = deque(a)
cnt = 0
while a:
    for _ in range(k-1):
        cur = a.popleft()
        a.append(cur)
    a.popleft()
    if len(a)==1:
        print(a[0])
        a.popleft()
