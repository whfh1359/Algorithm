leftli = []
rightli = []
N = int(input())
p = 100000
for i in range(1,N+1): # i 는 몇번째 input인지도 0부터 시작이라, i ==1이면 원소개수는 짝수, i %2 ==0 이면 홀수
    new = int(input())
    if new < p :
        leftli.append(new)
        leftli.sort()
        if i%2 == 0 : #짝수임
            o = leftli.pop() # 왼쪽중 젤 오른쪽 뻼
            print(o)
            print(leftli)
            rightli.insert(0,o)
    elif new > p:
        rightli.append(new)
        rightli.sort()
        if i%2 ==1 :
            o = rightli.pop(0)
            leftli.append(o)
    p = leftli[-1]
    print(p)
# sort를 이용하면, 시간복잡도가 증가해서, 

