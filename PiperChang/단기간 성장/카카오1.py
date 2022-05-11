def solution(alp, cop, problems):
    def findGoal() :
        goal = [0,0]
        for i in problems :
            goal[0] = max(goal[0],i[0]) 
            goal[1] = max(goal[1],i[1]) 
        return goal
    goal = findGoal()

    minimumCost = [[None for _ in range(300)] for _ in range(300)]

    def minCost(n1,n2) :
        if minimumCost[n1][n2] != None :
            return minimumCost[n1][n2]

        if n1 >= goal[0] and n2 >= goal[1] : # 성공하면 다음 놈 부를 필요가 없음            
            return 0

        possibleRoutes = []

        for prob in problems :
            if n1 >= prob[0] and n2 >= prob[1] :
                possibleRoutes.append(minCost(n1 + prob[2], n2 + prob[3]) + prob[4])
        if n1 < goal[0] :
            possibleRoutes.append(minCost(n1 + 1, n2) + 1)
        if n2 < goal[1] :
            possibleRoutes.append(minCost(n1, n2 + 1) + 1)
            
        minimumCost[n1][n2] = min(possibleRoutes)

        return minimumCost[n1][n2]
        
    return minCost(alp,cop)

