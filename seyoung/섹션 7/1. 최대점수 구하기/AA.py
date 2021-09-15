import sys
sys.stdin = open("in1.txt", "rt")

def DFS(L,start,time):
    global result
    print(L, start, time, path)
    if time>m:
        return
    if L ==n or time==m:
        if sum(path)>result:
            result = sum(path)
            # print("result :", result)
            # print()
        return
    else:
        for i in range(start,n):
            if ch[i] == 0:
                ch[i] = 1
                path.append(arr[i][0])
                DFS(L+1,i+1,time + arr[i][1])
                path.pop()
                ch[i] = 0

if __name__ =="__main__":
    n,m = map(int, input().split())
    # print(n, m)
    arr = []
    ch = [0]*(n+1)
    path = []
    result = -21470000
    for i in range(n):
        score, time = map(int, input().split())
        arr.append((score,time))
    # print(arr)
    DFS(0,0,0)
    print(result)
