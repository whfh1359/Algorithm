def solution(s):
    length = []
    result = ""
    for cut in range(1, len(s)//2+1):
        tmpstr = s[:cut]
        count = 1
        for i in range(cut,len(s),cut):
            if s[i:i+cut] == tmpstr:
                count +=1
            else:
                if count ==1:
                    count = ""
                result += str(count) + tmpstr
                tmpstr = s[i:i+cut]
                count = 1
        if count == 1:
            count = ""
        result += str(count) + tmpstr
        length.append(len(result))
        result = ""
    return min(length)

print(solution("aabbaccc"))