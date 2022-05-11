def solution(alp, cop, problems):
    def findGoal() :
        goal = [0,0]
        for i in problems :
            goal[0] = max(goal[0],i[0]) 
            goal[1] = max(goal[1],i[1]) 
        return goal

    goal = findGoal()

    # 줄여나가자.
    minimumCost = [[None for _ in range(300)] for _ in range(300)]
    minimumCost[alp][cop] = 0

    def minCost(al, co):
        print (al, co)
        if minimumCost[al][co] != None :
            return minimumCost[al][co]
        # 시작점 아래로 내려가는 방법은 아싸리 틀맀다
        if al < alp or al < cop :
            return 101
        # 풀수 있는 문제

        possibleRoutes = []
        
        for problem in problems :
            # 풀수 있으면,
            if alp - problem[2] >= problem[0] and cop-problem[3] >= problem[1] :
                possibleRoutes.append(minCost(alp-problem[2], cop-problem[3]) + problem[4])
        # if alp - 1 >= al : 짜피 al < alp 에서 다 걸렀음
        possibleRoutes.append(minCost(alp-1, cop) + 1)
        possibleRoutes.append(minCost(alp, cop-1) + 1)
        minimumCost[alp][cop] = min(possibleRoutes)
        
        return minimumCost[alp][cop]
    
    return minCost(goal[0],goal[1])
solution(10,10,[[10,15,2,1,2],[20,20,3,3,4]])