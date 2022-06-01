def solution(record):
    answer = []
    info = {}
    for x in record:
        split_x = x.split()
        if len(split_x) == 3:
            info[split_x[1]] = split_x[2]

    for x in record:
        split_x = x.split()
        if split_x[0] == "Enter":
            s_in = info[split_x[1]]+"님이 들어왔습니다."
            answer.append(s_in)
        if split_x[0] == "Leave":
            s_out = info[split_x[1]] +"님이 나갔습니다."
            answer.append(s_out)
    return answer
print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))
