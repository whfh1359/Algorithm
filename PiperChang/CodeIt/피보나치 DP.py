def fib_memo(n, cache):
    # 코드를 작성하세요.
    for i in range(2,n) :
        cache[i]= cache[i-1]+cache[i-2]
    return cache[n]

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
    fib_cache[1] = 1
#    for i in range(2,n) :
#        fib_cache[i]= fib_cache[i-1]+fib_cache[i-2]
    return fib_cache[n]
#    return print(fib_cache)


# 테스트
print(fib(10))
print(fib(50))
print(fib(100))

"""
def fib_memo(n, cache):
    # 코드를 작성하세요.
    #cache[]
    if n <3:
        return 1
    if n in cache :
        return cache[n]
    else :
        cache[n] = fib_memo(n-1,cache) + fib_memo(n-2,cache)
        return cache[n]
        
    

def fib(n):
    # n번째 피보나치 수를 담는 사전
    fib_cache = {}
 
    return fib_memo(n, fib_cache)

"""
