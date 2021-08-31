V,E = map(int, input().split())

# 간선들의 정보
tree = [ [] for i in V+1 ]
# 방문한 정점들
visited = [ 0 for i in V ]
# 다음에 갈 수 있는 정점들.
candidate = []

for i in range(E) :
    u, v, weight = map(int,input().split())
    tree[u].append([weight,u,v])
    tree[v].append([weight,v,u])

def prim(tree, startpoint):
    visited[startpoint] = 1
    candidate.append(tree[startpoint])
    # candidate에 startpoint 에서 

        
    u = 


visited[1] = 1
candidate = graph


# 처음엔 제일 가중치가 작은 애 넣기.
# dict에서 가중치가 제일 작은 애 찾기
# 최초에 시작할 정점을 넣어줘야함.

spanTree.append(1)
# 1이 가진 간선 정보들 전부 nextTree에 넣어줘야 함
# 접근 법은 맞는 것 같은데, 자료형들의 이용을 잘 못하는 것 같아.


for key in tree[1] :
    NextTree[key] = tree[1][key]

# print(NextTree)

for i in range(V-1) :
    # next 결정해야함
    minVal = 1000000
    for key in NextTree :
        if NextTree[key] < minVal :
            minKey = key
            minVal = NextTree[key]
    # 다음으로 연결될 정점은 현 span tree가 연결할 수 있는 가중치가 가장 작은 정점이다.
    next = minKey
    # 그 간선으로 연결되었기 때문에, minVal은 dist에 추가된다.
    spanTree.append(next)
    dist += minVal
    # tree 에서 next가 가진 간선들의 정보를 nextTree에 전부 잡아넣는다.
 
    # print(tree[next])
    for key in tree[next] :
        # print(key)
        # print(NextTree)
        if key not in spanTree :
            # span tree에 아직 안들어온 정점이어야 함.
            # 만약 nextTree랑 이미 연결되어 있는 정점이라면 더 가중치가 낮은 간선으로 대체  
            if key in NextTree :
                if NextTree[key]>tree[next][key] : # 다음으로 연결될 예비 중에 있으면
                    NextTree[key] = tree[next][key] # 더 짧은 애로 대체
            else : # nextTree에 연결 안되던 애면 걍 추가하면 됨!
                NextTree[key] = tree[next][key]
    # print(spanTree)
    NextTree.pop(next)


                    
                
        


print(dist)

    

