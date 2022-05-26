# function solution(N, relation, dirname) {
#     maxDirName = new Array(N+1).fill(0)
#     i = N
#     function maxLeng(dirNum) {
#         var li = [0];
#         if (maxDirName[dirNum] != 0) {
#             return maxDirName[dirNum]
#         }
#         /*for (i = 0; i < relation.length; i++) {
#             console.log(relation[i],relation[i][1])
#             if (relation[i][0] == dirNum) {
#                 li.push(maxLeng(relation[i][1]))
#                 //relation.splice(i,1)
#             }
#         }
#         */
#         for (var i of relation) {
#             if (i[0] == dirNum) {
#                 li.push(maxLeng(i[1]))
#                 relation = relation.filter((e)=> e !== i)
#             }
#         }
#         maxDirName[dirNum] = Math.max(...li)+dirname[dirNum-1].length + 1
#         return Math.max(...li)+dirname[dirNum-1].length + 1
#     }
#     answer = maxLeng(1)
#     return answer-1;
# }


def sol(N,relation,dirname) :
    # dfs로 길이를 알아야 한다는 거임
    lenTillThePoint = [0 for i in range(N)]

    def a(N):
        if N == 0 :
            return 4
        if lenTillThePoint[N] != 0 :
            return lenTillThePoint[N]
        else :
            for i in relation :
                if i[1] == N :
                    lenTillThePoint[N] = len(relation[N]) + a(i[0]) + 1
                    return lenTillThePoint[N]
    for i in reversed(range(N)) :
        a(N)
    max = 0

    for i in lenTillThePoint :
        max = max(max,i)
    return max
