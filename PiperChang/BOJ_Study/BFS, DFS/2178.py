N, M  = list(map(int,input().split()))

matrix = []
minval = 100*100

for i in range(N):
    matrix.append(list(input()))
visited = matrix
stack = []

# dfs의 핵심
def bfs():
    # 스택에 넣고 뺴기를 반복. 도착하면 min
    x = 1
    y = 1
    cnt = 1
    while x != M or y != N :
        print('ok')
        print(y<N)
        print(matrix[x][y+1])
        if x < M :
            if matrix[x + 1][y] :
                matrix[x+1][y] = 0
                stack.append([x + 1, y])
        if x > 0 :
            if  matrix[x - 1][y] :
                matrix[x - 1][y] = 0
                stack.append([x - 1, y])
        if y < N :
            if matrix[x][y + 1] :
                matrix[x][y + 1] = 0
                stack.append([x, y + 1])
        if y > 0:
            if matrix[x][y - 1]:
                matrix[x][y - 1] = 0
                stack.append([x, y - 1])
        print(stack)
        cnt += 1
        x,y = stack.pop(0)

bfs()