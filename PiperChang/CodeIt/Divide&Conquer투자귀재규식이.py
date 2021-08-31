def mid_sum_right(profits,start,end) :
    #중간서 오른쪽으로 갈 때의 합
    max_ = 0
    for i in range(start,end+1) :
        sum_of_sub = 0
        subPro = profits[start:i]#이 배열의 합
        for j in subPro :
            sum_of_sub = sum_of_sub + j
        max_ = max(sum_of_sub, max_)
  #  print(max_, "오른쪽 max")
    return max_
    
def mid_sum_left(profits,start,end):
    #중간서 왼쪽으로 갈 때의 합
    max_ = 0
    profits_ = list(reversed(profits[start:end+1]))
 #   print(profits_)
    for i in range(len(profits_)) :
        sum_of_sub = 0
        subPro = profits_[:i+1]
    #이 배열의 합
        for j in subPro :
            sum_of_sub = sum_of_sub + j
        max_ = max(sum_of_sub, max_)
#    print(max_, "왼쪽 max")
    return max_
    

#end 는 profits 길이 -1이다. 즉, start,end는 index 값이다.
#
def sublist_max(profits, start, end):
    # 코드를 작성하세요. 
    if (end-start == 0) : # 1개로 나뉘어지면,  
#        print("1개",start)
        if profits[start]>0:
            return profits[start]
        return 0
    mid = (start+end)//2 #중간의 index 값
#    print("profits[",start,",",end,"] mid는", mid)
    a = sublist_max(profits,start,mid)
    
   # print("a",a)
    b = sublist_max(profits,mid+1,end)
    #print("리턴한다.",end)

    #print("b",b)
    c = mid_sum_left(profits,start,mid) + mid_sum_right(profits,mid+1,end)
#    print("max",max(a,b,c))
    return(max(a,b,c))


# 테스트
list1 = [-2, -3, 4, -1, -2, 1, 5, -3]
print(sublist_max(list1, 0, len(list1) - 1))

list2 = [4, 7, -6, 9, 2, 6, -5, 7, 3, 1, -1, -7, 2]
print(sublist_max(list2, 0, len(list2) - 1))

list3 = [9, -8, 0, -7, 8, -6, -3, -8, 9, 2, 8, 3, -5, 1, -7, -1, 10, -1, -9, -5]
print(sublist_max(list3, 0, len(list3) - 1))

list4 = [-9, -8, -8, 6, -4, 6, -2, -3, -10, -8, -9, -9, 6, 2, 8, -1, -1]
print(sublist_max(list4, 0, len(list4) - 1))