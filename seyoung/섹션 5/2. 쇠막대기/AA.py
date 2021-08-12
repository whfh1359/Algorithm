import sys
sys.stdin = open("in1.txt", "rt")

a=list(str(input()))
stack = []
s=0
e=0
count = 0
for i in range(len(a)):
    if a[i] =='(':
        stack.append(a[i])
        s+=1
    elif a[i] ==')' and a[i-1] == '(':
        stack.pop()
        count += len(stack)
    elif a[i] == ')' and a[i-1] == ')':
        stack.pop()
        count += 1
print(count)


