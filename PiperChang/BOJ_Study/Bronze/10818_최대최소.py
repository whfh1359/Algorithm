#N개의 정수가 주어진다. 이때, 최솟값과 최댓값을 구하는 프로그램을 작성하시오.

def ans() :
    N = input()
    nList = list(map(int,input().split()))
    # list 함수는 Iterable 한 자료형을 넣으면, list로 반환해준다.
    # map 함수 역시, Iterable한 data와 자료형 이름을 넣으면,해당 자료형으로 변환한 map 객체를 반환해준다.  
    sN = nList[0]
    bN = nList[0]
    for i in nList:
        if (i > bN):
            bN = i
        elif (i < sN) :
            sN = i

    print(sN,bN)

ans()