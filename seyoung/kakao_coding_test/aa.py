from datetime import datetime
import math
def solution(fees, records):
    answer = []
    dic = {}
    for x in records:
        time, num, state = x.split()
        dic[num] = 0
    for x in records:
        time, num, state = x.split()
        if dic[num] != 0:
            k = dic[num]
            p = (datetime.strptime(time,"%H:%M")-k)
            p = p.seconds //60
            answer.append((num,p))
            dic[num] = 0
        else:
            dic[num] = datetime.strptime(time,"%H:%M")

    for x in dic.items():
        if x[1] !=0:
            p = datetime.strptime("23:59","%H:%M")-x[1]
            p = p.seconds //60
            answer.append((x[0],p))
    new_dic = {}
    for x in answer:
        new_dic[x[0]] = 0
    for x in answer:
        if new_dic[x[0]] != 0:
            k = new_dic[x[0]]
            k = x[1] +k
            new_dic[x[0]] = k
        else:
            new_dic[x[0]] = x[1]
    normal, normal_fee,m_h,m_h_price = fees[0],fees[1],fees[2],fees[3]
    for x in new_dic:
        if int(new_dic[x]) < normal:
            new_dic[x] = normal_fee
        else:
            new_dic[x] = normal_fee + (math.ceil((new_dic[x]-normal)/m_h))*m_h_price
    answer = []
    for x in sorted(new_dic.items()):
        answer.append(x[1])
    return answer

a = solution([180, 5000, 10, 600],
             ["05:34 5961 IN", "06:00 0000 IN", "06:34 0000 OUT",
              "07:59 5961 OUT", "07:59 0148 IN", "18:59 0000 IN",
              "19:09 0148 OUT", "22:59 5961 IN", "23:00 5961 OUT"],)
print(a)