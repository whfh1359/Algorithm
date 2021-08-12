import sys
sys.stdin = open("in1.txt", "rt")

a = list(range(1,21))
for i in range(10):
    temp = []
    n,m = map(int,input().split())
    for j in range(m-n+1):
        temp.append(a[m-j-1])
    a[n-1:m] = temp
for k in a:
    print(k, end = ' ')
