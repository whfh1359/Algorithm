def ans() : 
  n,k = map(int,input().split()) #입력이 '5 3'과 같이 한 줄에 스페이스 공백문자로 나뉘어져 들어오면, split()을 이용해, 하나씩 변수에 할당해 줄 수 있다.
  # map은 첫 parameter로 받은 자료형으로 2번째 param를 변경해준다.
  # n의 약수 중에서 K번째로 작은 수 출력
  # n보다 작은 수들을 하나씩 약수인지 확인해 보고, 약수일 때 마다, count를 +1 해서 k가 될 때의 수를 찾으면 된다.   
  count = 0
  for i in range(1,n+1):
    if n % i == 0 :
      count = count+1
      if count == k :
        print(i)
        return
  print(0)

ans()