n,k = input().split()

# 그리디 알고리즘 : 가치/무게가 가장 큰 것 순으로 넣을 것 
weight = 0
value = 0
items = []


for i in range(n):
    w,v = input().split()
    items.append([w,v,v/w])
    

while n >= weight :
    # 그리디로 풀리나