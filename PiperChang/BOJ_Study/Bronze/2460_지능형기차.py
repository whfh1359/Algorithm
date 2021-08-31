"""최근에 개발된 지능형 기차가 1번역(출발역)부터 10번역(종착역)까지 10개의 정차역이 있는 노선에서 운행되고 있다. 
이 기차에는 타거나 내리는 사람 수를 자동으로 인식할 수 있는 장치가 있다. 이 장치를 이용하여 출발역에서 종착역까지 가는 도중 기차
안에 사람이 가장 많을 때의 사람 수를 계산하려고 한다. 단, 이 기차를 이용하는 사람들은 질서 의식이 투철하여,
 역에서 기차에 탈 때, 내릴 사람이 모두 내린 후에 기차에 탄다고 가정한다."""

#가장 많을 때 찾아라~

def ans() :
    current = 0
    max = current
    for i in range(10) :
        minus, plus = map(int,input().split()) #input한 값은 str라는 것 잊지 말기
        current = current-minus + plus
        if current > max : 
            max = current
    print(max)

ans()
    # 매번 빼고, 더해서 계산
