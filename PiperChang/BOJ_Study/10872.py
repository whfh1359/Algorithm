N = int(input())

def getFactorial(N):
    if N <= 1 :
        return 1
    return getFactorial(N-1) * N
print(getFactorial(N))
