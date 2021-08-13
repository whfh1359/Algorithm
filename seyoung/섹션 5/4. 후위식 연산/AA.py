import sys
#sys.stdin = open("in1.txt", "rt")

a = input()
stack = []
for x in a:
    if x.isdecimal():
        stack.append(x)
    else:
        a = int(stack.pop())
        b = int(stack.pop())
        if x == '+':
            sum = b+a
            stack.append(sum)
        elif x== '-':
            dif = b-a
            stack.append(dif)
        elif x=='*':
            mul = b*a
            stack.append(mul)
        elif x=='/':
            div = b/a
            stack.append(div)
res = stack.pop()
print(res)
