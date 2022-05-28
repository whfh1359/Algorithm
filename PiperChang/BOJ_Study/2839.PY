N = int(input())

memo = [N for i in range(N+5)]
memo[3] = 1
memo[5] = 1
# 3개수, 5개수 더하기
def solution(N):
    if N == 4:
        return -1
    for i in range(3,N+1):
        a = min(memo[i-3], memo[i-5])
        if a != N :
            memo[i] = a + 1

    if memo[N] == N :
        return -1
    else :
        return memo[N]

print(solution(N))