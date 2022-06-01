import sys
sys.stdin = open("in1.txt", "rt")

def DFS(L, sum, time):
    global result
    if time>m:
        return
    if L==n:
        if sum>result:
            result = sum
    else:
        DFS(L+1, sum+pv[L], time+pt[L])
        DFS(L+1, sum, time)
if __name__=="__main__":
    n,m = map(int, input().split())
    pv = []
    pt = []
    result = -21470000
    for i in range(n):
        score, time = map(int, input().split())
        pv.append(score)
        pt.append(time)
    res = [0]*(n+1)
    DFS(0,0,0)
    print(result)