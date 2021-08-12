import sys
sys.stdin = open("in1.txt", 'rt')

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
for i in b:
    a.append(i)
a.sort()
for k in a:
    print(k, end = ' ')
