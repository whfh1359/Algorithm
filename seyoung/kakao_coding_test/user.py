from collections import deque
from collections import Counter
from itertools import product
from itertools import combinations

def solution(user_id, banned_id):
    answer = []
    cnt = 0
    tmp = list(set(combinations(user_id, len(banned_id))))
    a = product(tmp,banned_id)
    for x in a:
        print(x)
        print(x[0][1][0], x[1][1])
        s = ""
        result = False
        if len(x[0]) != len(x[1]): continue
        for i in range(len(x[0])):
            if x[0][i] == x[1][i]:
                result = True
                s = s + x[0][i]
            elif x[1][i] == "*":
                s += x[0][i]
                result = True
                continue
            else:
                result = False
                break
        if result :
            answer.append(x)
    print(answer)
#    b = list(set(combinations(answer,len(banned_id))))

#    for x in b:
#        print(x)
#        if Counter(x) == Counter(banned_id):
#            print(x)
#            cnt += 1
    return cnt