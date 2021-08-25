from collections import deque

def target_num(board, moves):
    for i in range(len(board)):
        if board[len(board)-1][moves-1] == 0:
            return 1000000
        elif board[i][moves-1] != 0:
            target_num = board[i][moves-1]
            board[i][moves-1] = 0
            break
    return target_num


def solution(board, moves):
    moves = deque(moves)
    bucket = []
    cnt = 0
    while moves:
        tmp = moves.popleft()
        target = target_num(board, tmp)
        if target == 1000000:
            break
        if len(bucket) == 0:
            bucket.append(target)
        else:
            bucket_top = bucket[-1]
            if target == bucket_top:
                bucket.pop()
                cnt += 2
            else:
                bucket.append(target)
    return cnt

a = solution([[0, 0, 0, 0, 0], [0, 0, 1, 0, 3], [0, 2, 5, 0, 1], [4, 2, 4, 4, 2], [3, 5, 1, 3, 1]], [1, 5, 3, 5, 1, 2, 1, 4])
print(a)