def solution(N, stages):
    result = {}
    total = len(stages)
    for i in range(1, N+1):
        if total != 0:
            failure = stages.count(i)
            result[i] = failure/total
            total -=failure
        else:
            result[i] = 0
    result = sorted(result,key = lambda x:result[x],reverse = True)
    return result