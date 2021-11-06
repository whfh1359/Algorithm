import sys
sys.stdin = open("in1.txt", "rt")

def DFS(L, sum):
    global cnt
    print(L, sum)
    if C[L] == 0:
        cnt +=1
    else:
        for i in range(1, len(P)+1):
            if C[i] !=0:
                C[L] -= 1
                DFS(L+1, sum+P[L])
                C[L] += 1
if __name__=='__main__':
    T = int(input())
    k = int(input())
    P = []
    C = []
    for i in range(k):
        p,c = map(int, input().split())
        P.append(p)
        C.append(c)
    cnt = 0
    DFS(0,0)
    print(cnt)
