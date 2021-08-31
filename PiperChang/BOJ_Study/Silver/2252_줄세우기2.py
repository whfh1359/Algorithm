# self coding한 것은, 기능은 되었으나, 시간초과로 해결에 실패하였다.
# 시간 복잡도가 n^2이기 때문.

N, M = map(int, input().split())
from collections import deque
queue = deque()
# 굳이 queue 안쓰고, list이용해도 상관없긴 했을 듯.
# 리스트랑, 진입 차수 리스트
# insert(0,x ) 수행시, 
inDegree = [0 for i in range(N+1)]
graph = [[] for i in range(N+1)]

# 간선과 진입차수에 대한 정보 받아드리기.
for i in range(M):
    a,b = map(int, input().split())
    inDegree[b] += 1        # b 의 in_degree가 늘어난다.
    graph[a].append(b)      # a 를 선행으로 가지는 리스트에 b를 추가한다.

# indegree 0인 애들 queue에 넣기.
# queue에서 하나씩 빼면서, 뺀 애들을 선행으로 가지는 (뺀 놈의 graph리스트) 애들의 indegree 감소시켜 만약, indegree ==0되면, 그 녀석은 queue에 또 넣어. 이를 queue가 텅빌때까지 반복
for i in range(1, N+1):
    if inDegree[i]==0:
        queue.append(i)

while queue :
    #queue에서 하나씩 빼면서,
    k = queue.pop()
    print(k, end = ' ')
    # 뺀 애들을 선행으로 가지는 (뺀 놈의 graph리스트) 애들의 indegree 감소시켜 
    for i in graph[k] :
        inDegree[i] -= 1
    #만약, indegree ==0되면, 그 녀석은 queue에 또 넣어. 이를 queue가 텅빌때까지 반복
        if inDegree[i] ==0 :
            queue.append(i)
  
    