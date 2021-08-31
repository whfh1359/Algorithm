def course_selection(course_list):
    # 코드를 작성하세요.
  ans = []
  finTime = (0,0)
  while (course_list[0]) :
    for i in course_list: 
      if i[1] < finTime[1]:#남은 시간중 가장 빨리 끝나는 경어
        finTime = i
    ans.append(finTime)
    # courseList에서 가장 빨리 끝나는 수업
    # 겹치는 수업 course_list에서 제외
    newList = []
    for j in course_list :
      if j[0] >= finTime[1]: #시작시간이 새로 넣은애 끝시간보다 빠르면? 삭제
       newList.append(j)
    course_list = newList
  


  





#ans 젤 늦은거 끝난느 시간보다, 시작하는 시간이 늦은 게 없을 때) :
    while (course_list) :
        fastStart = (10000,0)
        earlyFinishClass = (0,10000)
        for i in course_list:
            if  i[1] < earlyFinishClass[1] :
                earlyFinishClass = i
            if fastStart[0]>i[0]:
                fastStart = i
        ans.append(earlyFinishClass)
        
        for i in course_list:
          if(ans[len(ans)-1][1] > i[0]):
              course_list.remove(i)
        print(ans)
        #  
        #새로 들어온 애 끝나는 시간보다 시작이 빠르면 다 퇴출
    
    return ans
        

# 테스트
print(course_selection([(6, 10), (2, 3), (4, 5), (1, 7), (6, 8), (9, 10)]))
print(course_selection([(1, 2), (3, 4), (0, 6), (5, 7), (8, 9), (5, 9)]))
print(course_selection([(4, 7), (2, 5), (1, 3), (8, 10), (5, 9), (2, 5), (13, 16), (9, 11), (1, 8)]))
