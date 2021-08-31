def trapping_rain(buildings):
    # 코드를 작성하세요
    currBuilding = 0
    count = 0
    btw = 0
    water = 0
    for i in buildings :
      if (i> currBuilding) :
        water += count * currBuilding - btw
        currBuilding = i
        count = 0
      else : 
        btw += i
        count+=1
    
    currBuilding = 0
    count = 0
    btw = 0

    for i in reversed(buildings) :
      if (i> currBuilding) :
        water += count * currBuilding - btw
        currBuilding = i
      else : 
        btw += i
        count+=1

    return water
    #currBuilding과 i 사이 물량 세기 



    #현재 기둥 왼 오 확인. 가장 낮은 
    #상황 1 : 중간이 젤 낮음
    #상황 2 : 양 옆이 젤 낮음 
    #젤 높은애 찾기, 그  좌우로 젤 높은애 찾기 1st랑 2nd 사이의 물량 측정,  2nd 바깥쪽에 다음으로 큰애 찾기
    #젤 왼쪽 애 다음으로 만나는 왼 보다 큰애 => 그 사이 물량 계산, 그 다음으로 만나는 왼보다 큰 애 물량 계산 or 없으면, 그 다음으로 젤 큰애 사이 계산
  
# 테스트
print(trapping_rain([3, 0, 0, 2, 0, 4]))
print(trapping_rain([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]))