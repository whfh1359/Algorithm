'''
# 체스판 다시 칠하기
# 1. 좌측 위 시작 점이 W/B일 때, 2개 씩 쌍으로 조건 만족하는지 Ox로 이중 리스트 생성
# 2. 좌측 위 점 부터, 8개 중 o 개수 세고, 다음 라인8개 중 o 개수, 이런 식으로 각 시작 가능 점에서 o 개수 전부 세서 비교

b_start = "BWBWBWBW"
w_start = "WBWBWBWB"

test_matrix_b = [b_start,w_start,b_start,w_start,b_start,w_start,b_start,w_start]
test_matrix_w = [w_start,b_start,w_start,b_start,w_start,b_start,w_start,b_start]

M,N = list(int(x) for x in input().split())

matrix = list(x for x in input().split("\n"))

min = 8*8

def solve() :
#    시작점 설정
  for start1 in range(len(matrix)-8) : #mat의 m 중 start1 번째 라인 부터 비교
    for start2 in range(len(matrix[0])-8) : #라인의 n 중 start2 번째 문자 부터 비교
      count = 0
# 8*8개 점 비교
      for i in 8:
        for j in 8:
          if matrix[start1+i,start2+j]==test_matrix_b[i,j]:
            count += 1
      if count < min :
        min = count

    
solve()
print(min)
'''

b_start = "BWBWBWBW"
w_start = "WBWBWBWB"

test_matrix_b = [b_start,w_start,b_start,w_start,b_start,w_start,b_start,w_start]
test_matrix_w = [w_start,b_start,w_start,b_start,w_start,b_start,w_start,b_start]

min = 64

def solve() :  
# 입력받기
  M,N = [int(x) for x in input().split()]
  matrix = []#  list(x for x in input().split("\n"))
  for i in range(M):
    matrix.append(input())
  min = 64
#    시작점 설정
  for start1 in range(M-8+1) : #mat의 m 중 start1 번째 라인 부터 비교
    for start2 in range(N-8+1) : #라인의 n 중 start2 번째 문자 부터 비교
# 8*8개 점 비교
      count = 0
      for i in range(8):
        for j in range(8):
          if matrix[start1+i][start2+j] != test_matrix_b[i][j]:
            count += 1
      #min = min(min,count)
      if count < min :
        min = count
#matrix w 랑 비교
      count =0       
      for i in range(8):
        for j in range(8):
          if matrix[start1+i][start2+j] != test_matrix_w[i][j]:
            count += 1
      #min = min(min,count)
      if count < min :
        min = count

  print(min)

    
solve()