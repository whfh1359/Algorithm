def buildBridge() :
  ansList = []
  testCase = int(input())
  for k in range(testCase) :
    N,M = map(int,input().split())
    ans = 1

    for i in range(N) :
      ans = (M-i) * ans / (i+1)
# for문이 2번 돌면 속도가 느려져서 안되는 듯.... 18
#    for j in range(1,N+1) :
#      ans = ans / j
    ansList.append(ans)
  for i in ansList :
    print(int(i))
  
  
buildBridge()

# 이 문제의 포인트는 1.순열/조합 문제인지 알아차릴수 있는지, 2.순열 문제 해결 가능한지 이다.
####세영이안녕