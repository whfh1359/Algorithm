from collections import Counter
import sys
sys.stdin = open("in1.txt","rt")

N,T = map(int, input().split())
a = []
for _ in range(N):
    a.append(list(map(int, input().split())))
print(a)
pos = [start_pos+speed*T for start_pos, speed in a]

for i in range(N-1):
    if pos[i] > pos[i+1]:
        pos[i] = pos[i+1]
print(len(Counter(pos)))