import sys
sys.stdin = open("in1.txt", "rt")
n, k = map(int, input().split())
a = list(map(int, input().split()))
temp = set() #중복 제거해야해서

for i in range(n):
    for j in range(i+1, n):
        for m in range(j+1, n):
            temp.add(a[i]+a[j]+a[m])
temp = list(temp)
temp.sort(reverse = True)
#temp = temp.sort(reverse = True) # sort()는 반환값 없으므로 할당해주려면 sorted로 해야한다.
print(temp[k-1])
