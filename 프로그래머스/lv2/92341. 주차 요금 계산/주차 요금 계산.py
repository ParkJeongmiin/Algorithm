import math
from collections import defaultdict

def solution(fees, records):
    answer = []
    dic = {}
    sum_dic = defaultdict(int)
    check_dic = {}
    
    for record in records:
        time, number, state = record.split()
        hour, minute = map(int, time.split(':'))
        
        if state == 'IN':
            dic[number] = [hour * 60 + minute]
            check_dic[number] = hour * 60 + minute
        else:
            dic[number].append(hour * 60 + minute)
            sum_dic[number] += dic[number][1] - dic[number][0]
            del check_dic[number]
            
    if check_dic:
        for number, in_time in check_dic.items():
            sum_dic[number] += 23 * 60 + 59 - in_time
    
    sum_dic = sorted(sum_dic.items())
                     
    for _, time in sum_dic:
        print(time)
        if time > fees[0]:
            answer.append(fees[1] + (math.ceil((time - fees[0]) / fees[2])) * fees[3])
        else:
            answer.append(fees[1])
            
    return answer