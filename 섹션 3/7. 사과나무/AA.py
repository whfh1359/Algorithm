import sys
sys.stdin = open("in1.txt", "rt")

#이렇게 풀지 말랜다
'''
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
#print(a)
app = []
mid = n//2
num = 0
for i in range(n):
    if i == mid:
        app.append(a[mid][:])
    else:
        app.append(a[i][abs(mid-i):-abs(mid-i)])
for x in app:
    for j in x:
        num += j
print(num)

'''

n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2
for i in range(n):
    for j in range(s,e+1):
        res += a[i][j]
    if i<n//2:
        s-=1
        e+=1
    else:
        s+=1
        e-=1
print(res)
