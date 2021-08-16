import sys
sys.stdin = open("in6.txt","rt")

n=int(input())
pure_visit = [0]*8
visit = [0]*8
log_name = ['home','transfer','account_tab','enter_account_no','enter_transfer_amount',
            'transfer_decision','enter_password','transfer_complete']
a = [list(input().split(',')) for _ in range(n)]
for i in range(n):
    a[i][0] = a[i][0][0:10]+" "+a[i][0][11:19]
    for j in range(len(log_name)):
        if a[i][3] == log_name[j]:
            a[i][3] = j
a = sorted(a, key = lambda x : x[0])
for i in range(n):
    for j in range(8):
        if a[i][3] ==log_name[j]:
            pure_visit[j] +=1
for x in a:
    print(x)