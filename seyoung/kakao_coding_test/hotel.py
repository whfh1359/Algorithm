def solution(k, room_number):
    dic = {}
    answer = []
    for x in room_number:
        visited = [x]
        print(visited)
        while x in dic:
            x=dic[x]
            visited.append(x)
            print(visited)
#        dic[x] = x+1
        answer.append(x)
        print(answer, dic)
        for j in visited:
            dic[j] = x+1
            print(dic)
    return answer

a = solution(10, [1, 3, 4, 1, 3, 1])
print(a)