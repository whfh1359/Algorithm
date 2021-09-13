import sys
#sys.stdin = open("in1.txt", "rt")

def DFS(L,total):
    global result
    if L> result:
        return
    if total > price:
        return
    if total == price:
        if L < result:
            result = L
    else:
        for i in range(n):
            DFS(L+1,total+a[i])

if __name__ == "__main__":
    n = int(input())
    a = list(map(int, input().split()))
    price = int(input())
    result = 214700000
    a.sort(reverse = True)
    DFS(0,0)
    print(result)
