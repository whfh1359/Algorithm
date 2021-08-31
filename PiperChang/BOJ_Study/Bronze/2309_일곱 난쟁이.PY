def dwarf():
    a= list()
    sum = 0
    for i in range(9) :
        new = int(input()) 
        a.append(new)
        sum = sum + new
    a.sort() # sort()와 sorted(a)의 차이. sorted(a)는 정렬된 a를 반환해주고!, a.sort()는 반환이 아니고, 그냥 a에 대해 메소드를 실행해주는 것.
    for i in range(9) : # 원래 7개를 찾아서 하려했는데, 반대로 생각했음
        for j in range(i+1,9) :
            if (sum -a[i]- a[j] == 100) :
                del a[j]
                del a[i]
                return(a)
                
for i in dwarf() :
   print(i)