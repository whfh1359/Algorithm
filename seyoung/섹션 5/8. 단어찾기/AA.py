import sys
#sys.stdin = open("in1.txt", "rt")

n = int(input())
origin = []
tmp = []
for _ in range(n):
    origin.append(input())
for _ in range(n-1):
    tmp.append(input())
for i in range(n):
    if origin[i] not in tmp:
        print(origin[i])
