import sys
sys.stdin = open("in1.txt", "rt")

def DFS(L,total,f):
    global result
    if L == n :
        tmp = []
        for i in range(len(res)-1):
            tmp.append(res[i]+res[i+1])
            print(tmp)
        # print(sum(tmp[1:-1]))
        # print(sum(res), sum(tmp[1:-1])*(n-2),f)
        if (total + sum(tmp[1:-1])*(n-2)) == f:
            result.append(res[:])
            return
        return
        #     print(1)
        #     result.append(res)
    else:
        for i in range(n):
            if check[i] == 0:
                res[L] = i+1
                check[i] =1
                total += arr[i]
                DFS(L+1,total,f)
                check[i] =0
                total -= arr[i]
if __name__=="__main__":
    n, f = map(int, input().split())
    arr = list(range(1,n+1))
    print(arr)
    res = [0]*n
    check = [0]*n
    result = []
    DFS(0,0,f)
