def init():
    N,M = map(int,input().split())
    topo= {}
    for i in range(M) :
        b,a =  map(int,input().split())
        if (b not in topo) :
            topo[b] =[]
# 만들때는 [] 존재하다가. []이면, 그 key 채로 삭제한다.
# 
        if (a in topo) :
            topo[a].append(b)
        else :
            topo[a] = [b]
    print(topo)
    topo_sort(topo,N)
    # for key,value in topo.items() :
    #     # print(key)
    #     empty_dict(key,topo)
    # # for i in range(M):
        
# 

def topo_sort(topo,n) :
    for i in range(n) :
        for key, value in topo.items():
            if len(value) ==  0 :
                f = key
                del(topo[f])
                break;
        print(f)
        for key,value in topo.items():
            if f in value :
                value.remove(f)

init()

# def empty_dict(key,topo) :
#     # 만약, key 넣은 게 빈거면
#     if (key in topo and len(topo[key])!=0) :
#     # if (len(topo[key])!=0):  
#         empty_dict(topo[key][0],topo)
#         empty_dict(key,topo)
#     else :
#         print(key,end=' ')
#         # print(topo)
#         for k, value in topo.items() :
#             # print(value)
#             if key in value :
#                 value.remove(key)
    

