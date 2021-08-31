def merge(list1, list2):
    # 이전 과제에서 작성한 코드를 붙여 넣으세요!
    ans = []
    i=0; j=0
    while (i<len(list1) and j<len(list2)):
        if list1[i] > list2[j]:
            ans.append(list2[j])
            j+=1
        elif list2[j] >= list1[i] :
            ans.append(list1[i])
            i+=1
    if i>=len(list1) :
        for el in list2[j:] :
            ans.append(el)
    else :
        for el in list1[i:] :
            ans.append(el)
    return ans
    
# 합병 정렬
def merge_sort(my_list):
    # 코드를 입력하세요.
  if len(my_list) ==1 :
      return my_list
  mid = len(my_list)//2
  a = merge_sort(my_list[:mid])
  b = merge_sort(my_list[mid:])
#  print(a)
#  print(b)
  return merge(a,b)


# 테스트
print(merge_sort([1, 3, 5, 7, 9, 11, 13, 11]))
print(merge_sort([28, 13, 9, 30, 1, 48, 5, 7, 15]))
print(merge_sort([2, 5, 6, 7, 1, 2, 4, 7, 10, 11, 4, 15, 13, 1, 6, 4]))
