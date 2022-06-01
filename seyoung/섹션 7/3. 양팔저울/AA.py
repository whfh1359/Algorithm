import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L,sum):
    global res
    if L==n:
        if 0<sum<=s:
            res.add(sum)
    else:
        DFS(L+1, sum+W[L]) #추를 왼쪽
        DFS(L+1, sum-W[L]) #추를 오른쪽
        DFS(L+1, sum) # 추를 안놓는다.

if __name__=="__main__":
    n = int(input())
    W = list(map(int, input().split()))
    s = sum(W)
    res = set()
    DFS(0, 0)
    print(s-len(res))
