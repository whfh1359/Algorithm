#재귀함수와 스택
#반복문 여러번 쓰면 유연성이 떨어져서 재귀함수로 쓴다.

import sys
sys.stdin = open("in1.txt", "rt")

def DFS(x):
    if x > 0:
#여기서 밑에 두줄 바꾸면 오름차순, 내림차순이 된다.
        DFS(x-1)
        print(x)

if __name__=="__main__":
    n = int(input())
    DFS(n)