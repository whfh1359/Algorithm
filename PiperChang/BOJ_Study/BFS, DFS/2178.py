# from collections import deque
#
# N, M = map(int, input().split())
#
# graph = []
#
# for _ in range(N):
#     graph.append(list(map(int, input())))
#
#
# # 너비 우선 탐색
# def bfs(x, y):
#     # 이동할 네 가지 방향 정의 (상, 하, 좌, 우)
#     dx = [-1, 1, 0, 0]
#     dy = [0, 0, -1, 1]
#
#     # deque 생성
#     queue = deque()
#     queue.append((x, y, 1))
#
#     while queue:
#         x, y, cnt= queue.popleft()
#         if x == N-1 and y == M-1:
#             return cnt
#
#         # 현재 위치에서 4가지 방향으로 위치 확인
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#             # 위치가 벗어나면 안되기 때문에 조건 추가
#             if nx < 0 or nx >= N or ny < 0 or ny >= M:
#                 continue
#
#             # 벽이므로 진행 불가
#             if graph[nx][ny] == 0:
#                 continue
#
#             # 벽이 아니므로 이동
#             if graph[nx][ny] == 1:
#                 graph[nx][ny] = 0
#                 queue.append((nx, ny, cnt+1))
#
#     # 마지막 값에서 카운트 값을 뽑는다.
#     return cnt
#
#
# print(bfs(0, 0))

from collections import deque

N, M  = list(map(int,input().split()))
matrix = []

for i in range(N):
    matrix.append(list(map(int ,input())))

def bfs(x,y) :
    dx = [1, 0, -1, 0]
    dy = [0, -1,0, 1]
    queue = deque([(0,0,1)])

    while queue :
        x,y,cnt = queue.popleft()
        if x == N - 1 and y == M - 1:
            return cnt

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<= nx and nx < N and 0<= ny and ny < M :
                if matrix[nx][ny] == 1 :
                    matrix[nx][ny] = 0
                    queue.append((nx, ny, cnt+1))

print(bfs(1,1))