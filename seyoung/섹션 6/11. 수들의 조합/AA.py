import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L,start,total):
    global cnt
    if L==k:
        if total%m==0:
            # for x in res:
                # print(x, end = ' ')
            cnt+=1
        # print()
    else:
        for i in range(start, n):
            res[L] = arr[i]
            DFS(L+1,i+1,total + arr[i])

if __name__=='__main__':
    n,k = map(int, input().split())
    arr = list(map(int, input().split()))
    m = int(input())
    res = [0]*k
    cnt =0
    DFS(0,0,0)
    print(cnt)
