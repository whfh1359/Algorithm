import sys
sys.stdin = open("input.txt", "r")

def DFS(v):
    if v>7:
        return
    else:
        #print의 순서를 앞, 중간, 가운데로 하면 전위, 중위, 후위 순회 구현 가능
        DFS(v*2)
        DFS(v*2+1)
        print(v)

if __name__=="__main__":
    DFS(1)