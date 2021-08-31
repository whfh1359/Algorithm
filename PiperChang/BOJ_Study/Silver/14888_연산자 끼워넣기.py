# 1.깊이 우선 탐색으로, 재귀형태로 해결하였다. https://mytodays.tistory.com/9
# 각 상황이 일어날 때마다, if 문에서 다음 재귀로 넘어가는 것의 반복
# 함수 내에서, 전역 변수 이용하려면, global 변수명으로 이용해야한다.
N = int(input())
numlist = list(map(int,input().split())) # N개의 수가
oplist = list(map(int,input().split()))
anslist =[]
#젤 왼쪽 값이 acc 시작이어야 한다.

Num_min = 10000000000
Num_max = -10000000000

def findAns(index, acc, plus,minus,mult,div): #첫 index는 numlist[1]. acc = numlist[0], 젤 마지막은 numlist[n]까지 계산해야함. 
    if index==N : #index는 계산될 대상임. 즉 처음은 1 acc는 그전까지니깐 0
        global Num_max
        global Num_min
        Num_min = min(Num_min,acc)
        Num_max = max(Num_max,acc)
        return 

    if (plus): # operation 전의 index //  index기준  
        findAns(index+1, acc + numlist[index], plus-1, minus,mult,div)
    if (minus) :
        findAns(index+1, acc - numlist[index], plus, minus-1,mult,div )
    if (mult) :
        findAns(index+1,acc*numlist[index], plus, minus,mult-1,div )
    if (div) :
        if acc <0:
            findAns(index+1,(-acc // numlist[index]) * -1, plus, minus,mult,div-1 )
        else :
            findAns(index+1,acc // numlist[index], plus, minus,mult,div-1 )

findAns(1,numlist[0],oplist[0],oplist[1],oplist[2],oplist[3] )

print(Num_max)
print(Num_min)
"""

def permute(arr):
    result = [arr[:]]
    print(result)
    c = [0] * len(arr)
    i =0
    print(c)
    while i < len(arr):
        if c[i] < i :
            if i % 2 ==0:
                arr[0], arr[i] = arr[i], arr[0]
            else :
                arr[c[i]],arr[i] = arr[i], arr[c[i]]
            result.append(arr[:])
            


permute([1,2,3,1,1,1,3,2,3])














from itertools import permutations
N = int(input())
numlist = map(int,input().split()) # N개의 수가
oplist = list(map(int,input().split()))

print(numlist)
print(oplist)
#만들수 있는 계산식 다 만들어보기
# 0  n개 1 b개 2 c개 3 d개로 만들수 있는 순열 다 만들기
# 순열 만들기 문제임
ope = []

sunyul = list(map(''.join, permutations(ope)))

print(sunyul)

# def ans(acc, oplist):
#     if len(oplist) == 0 :
#         return acc
    
#     acc = acc + i
#     return ans(acc, aplist)
    
    """