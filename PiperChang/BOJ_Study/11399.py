N = int(input())
firstStep = int(input())
P1 = [0,firstStep]
P2 = [0,firstStep]

for i in range(2,N+1) :
    next = int(input())
    P1.append(P2[i-1] + next)
    P2.append(max(P1[i-2],P2[i-2]) + next)

print(max(P2[N],P1[N]))

#
# def sol(N):
#     if memo[N] :
#         return memo[N]
#     if
#
#     return sol()
#
# P = list(map(int,input().split()))
# P.sort()
# ans = 0
# wait = 0
# for i in P :
#     wait = wait+i
#     ans += wait



# 연속 3번 111은 안된다

