import sys
sys.stdin = open("in1.txt", "rt")

a=input()
print(a)
res = ''
stack= []
for x in a:
    if x.isdecimal():
        res += x
    elif x =='(':
        stack.append(x)
    elif x=='*' or x=='/':
        while stack and (stack[-1]=="*" or stack[-1] == '/'):
            res += stack.pop()
        stack.append(x)
    elif x=='+' or x=='-':
        while stack and stack[-1] != '(':
            res += stack.pop()
        stack.append(x)
    elif x==')':
        while stack and stack[-1] != '(':
            res +=stack.pop()
        stack.pop()

while stack:
    res += stack.pop()
print(res)
