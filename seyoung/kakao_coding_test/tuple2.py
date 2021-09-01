import re
from collections import Counter
def solution(s):
    s = Counter(re.findall('\d+', s))
    return list(map(int,[k for k,s in sorted(s.items(), key=lambda x: x[1], reverse = True)]))

a = solution("{{20,111},{111},{20,30,111}}")
print(a)