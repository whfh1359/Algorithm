import sys
sys.stdin = open("in1.txt","rt")

n, m = map(int, input().split())
# print(n,m)
board = [[0]*n for _ in range(n)]
for i in range(m):
    row, col, weight = map(int, input().split())
    board[row-1][col-1] = weight

for x in board:
    for j in x:
        print(j, end = ' ')
    print()
