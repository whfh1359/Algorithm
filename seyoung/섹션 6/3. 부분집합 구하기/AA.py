import sys
from itertools import combinations
sys.stdin = open("in1.txt", "rt")

def DFS(x):
    if x>n:
        for i in range(1,n+1):
            if check[i]==1:
                print(i, end=' ')
        print()
    else:
        check[x]=1 #집합에 속한다면
        DFS(x+1)
        check[x]=0 #집합에 안속한다면
        DFS(x+1)


if __name__=="__main__":
    n = int(input())
    check= [0]*(n+1)
    DFS(1)