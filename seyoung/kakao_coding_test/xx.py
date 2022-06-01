from itertools import combinations
from collections import Counter
def solution(n, info):
    a = []
    cnt = 0
    info_sum = 0
    for i in range(len(info)):
        a.append(info[i]+1)
        info_sum +=info[i] * (10-i)
    print(info_sum)
    print(a)
    new = []
    for i in range(len(a)):
        for j in range(a[i]):
            new.append(10-i)
    comb = list(combinations(new,n))
    possible = []
    for x in comb:
        flag = True
        key = set(x)
        Count_a = Counter(x)
        for j in key:
            if Count_a[j] < a[10-j]:
                flag = False
        if flag:
            possible.append(x)
    print(possible)
    maxx = -2147000
    maxx_x = []
    for x in possible:
        key = set(x)
        if sum(key)> maxx:
            maxx = sum(key)
            maxx_x.append((x,sum(key)))
    print(maxx_x)
    print(sorted(maxx_x, key=lambda x: (x[1],min(x[0])) ,reverse = True))


    answer = []
    return answer
a = solution(5,[2,1,1,1,0,0,0,0,0,0,0])
print(a)



