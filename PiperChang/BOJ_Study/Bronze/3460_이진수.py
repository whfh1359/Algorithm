def ans() : 
  t= int(input())

  inpList = []
  for i in range(t):
    a = int(input())
    inpList.append(a)
  
  for n in inpList :
    count = 0
    while (n>=1) :
      rest=n % 2
      if (n%2 ==1) :
        print(count,end = ' ') #print는 원래 print("어쩌고", end = '/n') 인 상태이다. end를 별도로 설정하면 이와 같이 바꿀 수도 있다.
      count = count +1
      n= n//2
    print('')

ans()