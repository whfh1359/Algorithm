import sys
sys.stdin = open("in1.txt", "rt")

a=input()
print(a)
res = ''
stack= []
for x in a:
    if x.isdecimal():
        print(x)
    elif x =='(':
        stack.append(x)
    elif x == '+' or x=='-':
        stack.append(x)
    elif x=='*' or x=='/':
        stack.append(1)
print(stack)
