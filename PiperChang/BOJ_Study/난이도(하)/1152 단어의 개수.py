

def solve() :
  
  str_spliced = []
  str_spliced= input().replace('\n',' ').split(" ")
  print(str_spliced)

  while '' in str_spliced:
    str_spliced.remove('')

  print(str_spliced)
  rst = len(str_spliced)
  print(rst)

solve()
