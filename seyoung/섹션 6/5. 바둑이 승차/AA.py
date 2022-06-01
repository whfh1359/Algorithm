import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L,sum,k):
    global result
    if sum + (total-k) < result:
        return
    if sum>c:
        return
    if L== n:
        if sum > result:
            result = sum
            return
    else:
        DFS(L+1, sum+a[L], k+a[L])
        DFS(L+1, sum, k+a[L])

if __name__=="__main__":
    c,n = map(int, input().split())
    a = []
    result = -214700000
    for i in range(n):
        a.append(int(input()))
    total = sum(a)
    DFS(0,0,0)
    print(result)
