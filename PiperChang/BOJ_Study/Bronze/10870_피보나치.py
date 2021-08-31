def fib(n,list) :
    if n == 1 :
        return 1
    elif n == 0:
        return 0
    else :
        return fib(n-1,list) + fib(n-2,list)
#재귀로 해결  . . . n이 1부터 시작하는지, 0부터 시작하는 지 구분할 것, list의 index를 가르키는 것인지, 1번째, 2번째 와 같은 .     

list = [0,1]
n = int(input()) 

print(fib(n,list))