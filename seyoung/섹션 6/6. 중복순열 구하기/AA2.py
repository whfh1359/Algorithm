from itertools import product
import sys
sys.stdin = open("in1.txt", "rt")

n, m =map(int, input().split())
for i in product(range(1,n+1), repeat=m):
    print(i)