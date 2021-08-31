numCheck ={}
maxCount = []
def solve() :
  ans = 0
  string = input().upper()
  for a in string :
    if (a in numCheck) :
      numCheck[a] += 1
    else :
      numCheck[a] = 1
# 각 알파벳의 개수 세기
# 가장 많은 개수 찾기  
  for max in numCheck.values() :
    if max > ans :
      ans = max
  for key, val in numCheck.items(): #오류 출력
    if val == ans :
      maxCount.append(key)

  if len(maxCount) > 1:
    print("?")
  else :
    print(maxCount[0].upper())
  return
solve()
