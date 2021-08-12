import sys
sys.stdin = open("in1.txt", "rt")

n= int(input())
a = [list(map(int, input().split())) for _ in range(n)]
largest = -21470000

for i in range(n):
    row= col = 0
    for j in range(n):
        row += a[i][j]
        col += a[j][i]
    if row > largest:
        largest = row
    if col > largest:
        largest = col
sum1=sum2=0
for i in range(n):
    sum1 += a[i][i]
    sum2 += a[i][n-i-1]
if sum1 > largest:
    largest = sum1
if sum2 > largest:
    largest = sum2
print(largest)