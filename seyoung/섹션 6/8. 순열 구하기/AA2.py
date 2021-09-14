import sys
sys.stdin = open("in1.txt","rt")

def DFS(L,total):
    if L==3:
        print(res)
        result.append(total)
        return
    else:
        for i in range(len(arr)):
            if check[i] == 0:
                check[i] = 1
                res[L] = i+1
                total += arr[i]
                DFS(L+1,total)
                check[i] = 0
                total -= arr[i]

if __name__=="__main__":
    arr = [1,2,3,4,5]
    check = [0]*len(arr)
    res = [0]*3
    result = []
    DFS(0,0)
    print(result)