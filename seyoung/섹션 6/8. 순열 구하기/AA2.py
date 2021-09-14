import sys
sys.stdin = open("in1.txt","rt")

def DFS(L,total,count):
    if L==count:
        print(res)
        result.append(total)
        return
    else:
        for i in range(len(arr)):
            if check[i] == 0:
                check[i] = 1
                res[L] = i+1
                total += arr[i]
                DFS(L+1,total,count)
                check[i] = 0
                total -= arr[i]

if __name__=="__main__":
    arr = [1,2,3,4]
    check = [0]*len(arr)
    result = []
    for i in range(1,len(arr)+1):
        res = [0] * i
        DFS(0,0,i)
    print(result)