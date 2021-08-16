import collections
from collections import Counter

def solution(s):
    s.lower()
    answer = ''
    counter = collections.Counter(s).most_common()
    max_alpha = collections.Counter(s)
    print(max_alpha)
    for i in range(len(counter)):
        if counter[i][1] == counter[0][1]:
            if counter[i][0] == 't':
                answer += counter[i][0].upper()
            elif counter[i][0] == 'o':
                answer += counter[i][0].upper()
            elif counter[i][0] == 's':
                answer += counter[i][0].upper()
                answer += counter[i][0].upper()
            else:
                answer += counter[i][0]
    answer = sorted(list(answer))
    '''
    for x in answer:
        if x== 'T':
            answer.remove('T')
            answer.insert(0, 'T')
    '''
    return ''.join(answer)

a = solution("sqotdsdryetvtutsoowdeodevvsve")
print(a)
