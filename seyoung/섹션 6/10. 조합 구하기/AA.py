import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L, start):
    global cnt
    if L==m :
        for x in res:
            print(x, end= ' ')
        print()
        cnt +=1
    else:
        for i in range(start,n+1):
            res[L] = i
            DFS(L+1,i+1)
if __name__=="__main__":
    n, m = map(int, input().split())
    res = [0]*m
    cnt = 0
    DFS(0,1)
    print(cnt)
