"""# bottom to top 구조

def max_profit_memo(price_list, count, cache):
    for i in range(count+1) : #count까지 cache를 채운다. range는 그 숫자 전까지 채움
        if i < len(price_list) : #기본 price_list 단위 값이면 
            lr = price_list[i] #자기 값과 그 이전 단꼐들 합 값 비교
            for j in range(1,i): #이전 단계들
                num = cache[i-j] + price_list[j] 
                #price_list[i-j] + price_list[j]는 안된다. 
                #왜냐하면, price_list[i-j] 자체가 최적화된 상태가 아니기 때문
                if lr < num :
                    lr = num
            cache[i] = lr #기본 단계 끝
        else : 
            lr = 0
            for k in range(1,len(price_list)) : #현재 k에서,price list에 있는 최소 단위들 만큼 차이나는 애들의 값 + 그 단위 값 중 최대값.
                num = cache[i-k]+price_list[k]
                if ( num > lr ):
                    lr = num
                    cache[i] = lr
#        print(i)# + '명에게 팔면' + cache[count])
    return cache[count]

                
        
    #price_list는 0명부터 
    #결과값은 cache[count]여야 함.
    

def max_profit(price_list, count):
    max_profit_cache = {}
    
    return max_profit_memo(price_list, count, max_profit_cache)


# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))

"""
def max_profit_memo(price_list, count, cache): #cache에 count일 때 최대 profit 
  if count in cache : #이미 저장된 값일 때 
    return cache[count]
  profit = 0
			
	
  if count < len(price_list) : # 제일 작을 때
    profit = price_list[count]
    for i in range(count) :
      profit = max(profit,(max_profit_memo(price_list,count-i,cache) + max_profit_memo(price_list,i,cache)))  
    cache[count] = profit
    return profit 

  for i in range(1,len(price_list)):
    profit = max(profit,(max_profit_memo(price_list,count-i,cache) + max_profit_memo(price_list,i,cache)))
  cache[count] = profit	
  return profit
	             
def max_profit(price_list, count):
  max_profit_cache = {}
	
  return max_profit_memo(price_list, count, max_profit_cache)
	
	
	# 테스트
print(max_profit([0, 100, 400, 800, 900, 1000], 5))
print(max_profit([0, 100, 400, 800, 900, 1000], 10))
print(max_profit([0, 100, 400, 800, 900, 1000, 1400, 1600, 2100, 2200], 9))