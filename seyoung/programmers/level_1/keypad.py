def solution(numbers, hand):
    answer = ''
    dir = {"left" : 10, "right":12}
    for x in numbers:
        if x ==1 or x==4 or x==7:
            answer += "L"
            dir["left"] = x
        elif x==3 or x==6 or x==9:
            answer += "R"
            dir["right"] = x
        else:
            if x == 0:
                x = 11
            move_L = abs(x-dir["left"])%3 + abs(x-dir["left"])//3 #이동거리
            move_R = abs(x-dir["right"])%3 + abs(x-dir["right"])//3
            if move_L > move_R:
                answer += "R"
                dir["right"] = x
            elif move_L == move_R:
                if hand =="right":
                    answer += "R"
                    dir["right"] = x
                else:
                    answer += "L"
                    dir["left"] = x
            else:
                answer += "L"
                dir["left"] = x

    return answer

print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5], "right"))
print(solution([1, 2, 3, 4, 5, 6, 7, 8, 9, 0], "right"))