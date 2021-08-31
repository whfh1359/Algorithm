# 소수 구하는 코드 정도는 외워두자. 내가 이용한 방식은 '에라토스테네스의 체' 라는 방식이다.
# python은 List.remove() 가 있어서 비교적 쉽게 구현할 수 있었던 것 같다.

def init() :
    M = int(input())
    N = int(input())
    
    sosuList = []
    numList = []
    for i in range(2,N+1):
        numList.append(i)

    while(len(numList) != 0):
        sosu = numList[0]
        if (sosu>=M and sosu <= N):
            sosuList.append(sosu)
        for i in numList:
            if i % sosu == 0 :
                numList.remove(i)

    if (len(sosuList)==0) :
        print(-1)
    else :
        sum = 0
        for i in sosuList:
            sum= sum + i
        print(sum)
        print(sosuList[0])
    
    

init()        





#실패 : recurtion error 발생.

"""
def ans(sosuList,list) : #n to m의 소수 합을 받는다.
    if len(list) == 0 : #list 가 없으면, 재귀를 끝낸다.
        return sosuList
    sosu = list[0]
    if (sosu>= M and sosu<=N) :
        sosuList.append(sosu)
    #N 보다 큰 첫 소수는?
    #list[0]은 소수임.
    alist= [] #sosu 가능성 있는 애들 alist에 넣을 것.
    for i in list :
        if i % sosu != 0 :
            alist.append(i)
    return ans(sosuList,alist)# 가능성 있는 애들 데리고, 소수 찾아봐~
def sosu():
    for i in list:
        

M= int(input())
N= int(input())

list = []
sosuList = []

for i in range(2,N+1) : #N까지의 수를 모두 담은 list 
    list.append(i) 


a = ans(sosuList,list) #N까지의 소수 전부 return
sum= 0
for i in a:
    sum = sum + i
print(a[0])
print(sum)
    #소수 M이상 N이하의 수 중 소수 모두 고르기.
    #이 소수들의 합과 최솟값 구하기
    #재귀형태로 해보자.
# recursion Error 났다... 소수 마다 하기는 힘든가 보다.ㅋ    






"""
