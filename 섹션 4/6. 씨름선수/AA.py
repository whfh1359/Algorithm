import sys
sys.stdin = open("in1.txt", "rt")

n = int(input())
player = []
for i in range(n):
    h, w = map(int, input().split())
    player.append((h,w))
player.sort(reverse = True)
largest = 0
cnt = 0
for h,w in player:
    if w > largest:
        largest = w
        cnt +=1
print(cnt)
