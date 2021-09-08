from itertools import product
from itertools import combinations
def solution(user_id, banned_id):
    answer = []
    a = list(combinations(user_id, len(banned_id)))
    for i in range(len(a)):
#        print(a[i], len(a[i]))
        for k in range(len(a[i])):
            print(i,k)
            print("a[i][k],banned_id[i]", a[i][k],banned_id[i])
            for j in range(len(a[i][k])):
                flag = True
                if len(a[i][k]) != len(banned_id[i]):
                    flag = False
                    break
                print(j)
                print("a[i][j][j]", a[i][k][j])
                # print("banned_id[i]",banned_id[i])
                # print("banned_id[i][j]",banned_id[i][j])
                if banned_id[i][j] == "*":
                    continue
                # for h in range(len(a[i][j]))
                elif a[i][k][j] != banned_id[i][j]:
                    flag = False
                    break
            if flag:
                answer.append(a[i])
                print("answer",answer)
    return set(answer)


a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["*rodo", "*rodo", "******"])
print(a)
