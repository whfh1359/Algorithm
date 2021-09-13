def solution(board, skill):
    answer = 0
    for x in skill:
        start, end,step = (x[1],x[2]),(x[3],x[4]),x[5]
        for i in range(x[1],x[3]+1):
            for j in range(x[2],x[4]+1):
                k = board[i][j]
                if x[0] ==1:
                    k = k-x[5]
                    board[i][j] = k
                else:
                    k = k+x[5]
                    board[i][j] = k
    for x in board:
        for j in x:
            if j>0:
                answer+=1
    return answer

a = solution([[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5],[5,5,5,5,5]],
             [[1,0,0,3,4,4],[1,2,0,2,3,2],[2,1,0,3,1,2],[1,0,1,3,3,1]])
print(a)