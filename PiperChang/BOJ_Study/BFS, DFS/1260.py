N, M, V = map(int, input().split())

edgeList = {i: [] for i in range(N + 1)}

for i in range(M):
    edge = list(map(int, input().split()))
    edgeList[edge[0]].append(edge[1])
    edgeList[edge[1]].append(edge[0])

for key, val in edgeList.items():
    val.sort()

def BFS() :
    visited = {}
    visited[V] = True
    stack = [V]

    while( len(stack) != 0 ) :
        p = stack.pop(0)
        print(p, end=' ')
        for i in edgeList[p] :
            if i not in visited :
                stack.append(i)
                visited[i] = True

def DFS():
    visited = {}
    def DFSf(p) :
        visited[p] = True
        print(p, end = " ")
        for i in edgeList[p]:
            if i not in visited :
                DFSf(i)
    DFSf(V)
DFS()
print('')
BFS()

        #인접리스트에 있는거 끝까지 가버려 ( 긍까, 내가 찍은 곳 -> 그 곳에 연결된 점.  )
