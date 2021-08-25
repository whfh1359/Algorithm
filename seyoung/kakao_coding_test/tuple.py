from collections import deque
def max_num(x,y):
    max = 1
    for x,y in answer:
        y = int(y)
        x = int(x)
        if y-x > max:
            max = y-x
    return max

def solution(s):
    answer = []
    tmp = []
    for i in range(0,len(s)):
        if s[i] == '{' and s[i+1] != '{':
            left = i+1
            right = left
            #print(left)
            while s[right] != '}':
                right +=1
            answer.append([left,right])
            tmp = []
    t = max_num
    for x,y in answer:
        a = int(y)
        b = int(x)
        if b-a == t:
            answer[-1] = x,y
    return list(map(int, s[answer[-1][0]:answer[-1][1]].split(',')))

a = solution("{{22},{22,1},{22,1,3},{22,1,3,4}}")
print(a)