
def ans():
    a, b = map(int,input().split())
    # i를 i번씩 넣은 수열에서, 그 수열의 a번째 수부터, b번째 수까지의 합을 구하라. (a번째와 b번째도 포함) < 매우 중요한 포인트
    # 각 변수 끼리의 범위가 헷갈려서 계속 숫자를 바꿔가면서 풀었다. 처음에 확실히 시작이 포함되는지, 끝이 포함되는지 픽스할 것.

    count = 0 # 수열의 몇 번 째 자리인가
    i = 1     # i가 i번씩 수열을 채운다.
    ans = 0   # 답

    while(count<=b) : #count 가 b를 넘으면, 끝난다.(이는, i를 i개 넣은게 딱 끝났을 때만, 조건문이 발휘된다.)  
        for j in range(i): # i 를 i번 넣는다.
            count += 1 
            #i가 들어가면, count 번째 수에 대해 계산했다. ex) 1번째 수는 
            if (count >= a and count <=b) :           #  a 보다 크거나 같고, b보다는 작거나 같다.  . 
                ans = ans + i                         #  a번째 수, b번째 수는 모두 범위에 포함된다.
            elif (count>b):
                print(ans)
                return
        i+=1           
ans()