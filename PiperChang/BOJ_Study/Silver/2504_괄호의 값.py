def stack(): # pop 할 때, 수를 넣기. 만약 pop했는데, top 바로 아래에 이미 숫자가 있다면, 그 숫자와 새 숫자를 더하여,,push하기 
    inputList = list(input())
    stack = [["끝",0]] # push 및 pop
    for i in inputList:
        if (i =='(' or i =='['):
            stack.append([i,0])

        elif (i ==')'):           
            a = stack.pop()
            if a[0] != '(' :
                print(0)
                return
            if a[1] != 0 :
                stack[-1][1] =stack[-1][1] + (2 * a[1])
            elif a[1] ==0:
                stack[-1][1] =stack[-1][1] + 2

        elif (i == ']') :
            a = stack.pop()
            if a[0] != '[' :
                print(0)
                return
            if a[1] != 0 :
                stack[-1][1] =stack[-1][1] + (3 *a[1])
            elif a[1] ==0:
                stack[-1][1] =stack[-1][1] + 3
            
    print(stack[0][1])
            
stack()
            



"""
            a = 2
            stack.pop()
            if (type(stack[-1]) == type(1)) :
                a = a + stack.pop()
            stack.append(a)

    print()
        elif (i== ']') :
            a = 3
            stack.pop()
            if (type(stack[-1]) == type(1)) :
                a = a + stack.pop()
            stack.append(a)

    ans = 0
    acc = 1
    for i in inputList: 
        print(ans)
        print(stack)       
        if (i == '(' or i =='[') :
            
            stack.append(i)
        elif (i == ')'):
            if ('(' == pop(stack)):
                acc = acc *2
            else :
                return 0
        elif (i ==']') :
            if('[' == pop(stack)) :
                acc =acc *3
            else : 
                return 0
        if len(stack) == 0:
            ans = ans + acc
            acc = 1
    print(ans)
stack()      
"""
