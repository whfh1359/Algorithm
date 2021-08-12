#import sys
#sys.stdin = open("in1.txt","rt")

n = int(input())
a = list(map(int, input().split()))
M = int(input())
a.sort()
for _ in range(M):
    a[-1] -=1
    a[0]+=1
    a.sort()
print(a[-1]-a[0])
