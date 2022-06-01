import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L, sum):
    global result
    if L==n+1:
        if sum>result:
            result = sum
    else:
        if L+times[L]<=n+1:
            DFS(L+times[L], sum+prices[L])
        DFS(L+1, sum)
if __name__=="__main__":
    n = int(input())
    times = []
    prices = []
    for i in range(n):
        t, p = map(int, input().split())
        times.append(t)
        prices.append(p)
    times.insert(0,0)
    prices.insert(0,0)
    result = -21470000
    DFS(1,0)
    print(result)
