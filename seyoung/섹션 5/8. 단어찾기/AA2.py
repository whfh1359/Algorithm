import sys
sys.stdin = open("in1.txt", "r")

n = int(input())
p = dict()
for i in range(n):
    word = input()
    p[word] = 1
for i in range(n-1):
    word = input()
    p[word] =0
for key, value in p.items():
    if value == 1:
        print(key)
        break

'''
from collections import Counter
import sys
#sys.stdin = open("in1.txt", "rt")
a = []
for _ in range(2):
    a.append(input())
for i in range(1):
    if Counter(a[i]) == Counter(a[i+1]):
        print("YES")
    else:
        print("NO")
'''