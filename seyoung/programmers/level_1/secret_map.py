def solution(n, arr1, arr2):
    arr_1_board = []
    arr_2_board = []
    answer = []
    for x in arr1:
        a = str(bin(x)[2:])
        while len(a) < n:
            a = "0" + a
        arr_1_board.append(list(map(int, a)))
    for x in arr2:
        b = str(bin(x)[2:])
        while len(b) < n:
            b = "0" + b
        arr_2_board.append(list(map(int, b)))

    for i in range(n):
        for j in range(n):
            if arr_2_board[i][j] != arr_1_board[i][j]:
                arr_1_board[i][j] = 1
    for i in range(n):
        for j in range(n):
            if arr_1_board[i][j] == 1:
                arr_1_board[i][j] = "#"
            else:
                arr_1_board[i][j] = " "
    for x in arr_1_board:
        result = "".join(x)
        answer.append(result)
    return answer