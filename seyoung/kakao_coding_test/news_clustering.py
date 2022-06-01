def solution(str1, str2):
    tmp1 = []
    tmp2 = []
    for i in range(len(str1)-1):
        tmp = str1[i] + str1[i+1]
        tmp = tmp.lower()
        tmp1.append(tmp)
    for i in range(len(str2)-1):
        tmp = str2[i] + str2[i+1]
        tmp = tmp.lower()
        tmp2.append(tmp)
    str1 = list(filter(str.isalpha,tmp1))
    str2 = list(filter(str.isalpha,tmp2))
    if len(str1)==0 and len(str2)==0:
        return 65536

    a = str2.copy()
    b = str2.copy()

    #union
    for x in str1:
        if x not in b:
            a.append(x)
        else:
            b.remove(x)

    common = []
    b1 = str2.copy()
    #intersection
    for x in str1:
        if x in b1:
            b1.remove(x)
            common.append(x)
    return int((len(common)/len(a))*65536)

#a = solution('FRANCE','french')
a = solution('aa1+aa2','AAAA12')
print(a)