from collections import deque
def solution(s):
    answer = []
    tmp = []
    for i in range(0,len(s)):
        if s[i] == '{' and s[i+1] != '{':
            left = i+1
            right = left
            while s[right] != '}':
                right +=1
            answer.append([left,right])
    answer.sort(key=lambda x : x[:][0]-x[:][1], reverse = True)
    for x,y in answer:
        a = int(x)
        b = int(y)
        tmp.append(list(map(int, s[a:b].split(','))))
    real_answer =[]
    real_answer.append(tmp[0][0])
    for i in range(1, len(tmp)):
        for j in range(len(tmp[i])):
            if tmp[i][j] not in real_answer:
                real_answer.append(tmp[i][j])
    return real_answer

a = solution("{{20,111},{111},{20,30,111}}")
print(a)