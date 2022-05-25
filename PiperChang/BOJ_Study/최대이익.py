def solution(prices) :
    maxval = 0
    benefit = -10000000
    # max value가 바뀌면,
    for i in prices :
        benefit = max([maxval - i, benefit])
        if i > maxval :
            maxval = i

    return benefit

print(solution([3, 1, 4, 1, 5, 9, 2, 6, 5, 3]))