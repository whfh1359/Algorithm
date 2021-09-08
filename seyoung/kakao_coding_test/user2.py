from itertools import product
from itertools import combinations
from itertools import permutations
def solution(user_id, banned_id):
    answer = []
    a = list(permutations(user_id, len(banned_id)))
    # print(len(a))
    for i in range(len(a)):
        flag = True
        for k in range(len(a[i])):
            if flag == False:
                break
            if len(a[i][k]) != len(banned_id[k]):
                flag = False
                break
            # print("a[i][k],banned_id[i]", a[i][k],banned_id[k])
            for j in range(len(a[i][k])):
                # print(a[i], banned_id[k])
                # print("a[i][k][j]", a[i][k][j])
                # print("banned_id[i]",banned_id[i])
                # print("banned_id[k][j]",banned_id[k][j])
                if banned_id[k][j] == "*":
                    continue
                # for h in range(len(a[i][j]))
                elif a[i][k][j] != banned_id[k][j]:
                    flag = False
                    break
        if flag:
            a[i] = set(a[i])
            if a[i] not in answer:
                answer.append(a[i])
                # print("answer",answer)
    return len(answer)


a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"], ["fr*d*", "*rodo", "******", "******"])
print(a)
