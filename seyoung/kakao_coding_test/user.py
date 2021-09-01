import re
from collections import Counter
def solution(user_id, banned_id):
    s = Counter(re.findall('[a-zA-Z]',user_id))
    return s

a = solution(["frodo", "fradi", "crodo", "abc123", "frodoc"],["fr*d*", "abc1**"])
print(a)