def solution(board, moves):
    a = []
    cnt = 0
    # for x in board:
    #     print(x)
    for item in moves:
        for i in range(len(board)):
            if board[i][item-1] ==0:
                continue
            else:
                dolls = board[i][item - 1]
                # print(dolls)
                board[i][item - 1] = 0
                if len(a) ==0:
                    a.append(dolls)
                else:
                    q = a.pop()
                    if q == dolls:
                        cnt +=2
                    else:
                        a.append(q)
                        a.append(dolls)
                break
        # print(a)
    # for x in board:
        # print(x)
    return cnt

print(solution([[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               [1,5,3,5,1,2,1,4]))
