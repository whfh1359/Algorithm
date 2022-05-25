

'''
# 헐...
def prime(M,N):

    list = [i for i in range(2,N+1)]
    tmp = []
    decimalList = []
    while len(list) != 0 :
        dec = list.pop(0)
        length = len(list)
        for i in range(length) :
            if list[i] % dec !=0 :
                list.append(list[i])
        if dec >= M:
            print(dec)
        list = list[length:]
#
M, N = list(map(int,input().split()))
'''
M, N = list(map(int,input().split()))

# decimal은 0.~~ 인 소수이고, prime이 나눠지지 않는 수 소수이다.
def prime(M,N) :
    primeList = []
    for i in range(M,N+1):
        if i == 1 :
            continue
        primeList.append(i)
        for j in range(2, int(i**0.5)+1) :
            if (i % j == 0) :
                primeList.pop()
                break;
    for i in primeList :
        print(i)

prime(M,N)
'''
def decimal(M,N):
    list = [i for i in range(2,N+1)]
    decimalList = [0 for i in range(N)]
    for i in range(M) :

        def dcm(M, N):
            for i in range(M, N + 1):
                if i == 1:
                    continue
                for j in range(2, int(i ** 0.5) + 1):
                    if i % j == 0:
                        break;
                else:
                    print(i)
'''