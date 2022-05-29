N, M = map(int, input().split())
matrix = []
for i in range(N) :
    matrix.append(list(map(int,input().split())))


dx = [1,-1, 0 ,0]
dy = [0, 0, 1, -1]


def rollEast(rx,ry, bx,by):
    #북
    if max[x-1][y] == ".":
        while True:
            if matrix[x-i][y] == 'O':
                return cnt
            if matrix[x-i][y] != '#':

                break;
        rollNorth()
    if max[x][y] == "."


def rollRed(cnt, ):

    # 북쪽
    while True:
        if matrix[x-i,y] == 'O':
            return cnt
        if matrix[x - i, y] != '#' :
            break;
    # 동쪽
    while True:
        if matrix[x, y+i]== 'O':
            return cnt
        if matrix[x, y+i] != '#' :

            break;
    # 남쪽
    while True:
        if matrix[x-i,y] == 'O':
            return cnt
        if matrix[x-i, y] != '#' :
            break;
    # 서쪽
    while True:
        if matrix[x,y - i] == 'O':
            return cnt
        if matrix[x, y - i] != '#' :
            break;

def rollBlue(cnt,):
