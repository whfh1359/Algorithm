#import sys
sys.stdin = open("in1.txt", "rt")

n= int(input())
front = []
end = []
for i in range(n):
    s = input().upper()
    if s==s[::-1]:
        print("#%d YES" %(i+1))
    else:
        print("#%d NO" %(i+1))
