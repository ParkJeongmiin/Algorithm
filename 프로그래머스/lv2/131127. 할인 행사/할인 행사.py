from collections import Counter

def solution(want, number, discount):
    answer = 0
    
    want_dic = dict()
    for i in range(len(want)):
        want_dic[want[i]] = number[i]
        
    want_dic_counter = Counter(want_dic)

    # slicing
    for idx in range(0, len(discount) - 9):
        discount_counter = Counter(discount[idx : idx + 10])
        if len(want_dic_counter - discount_counter) == 0:
            answer += 1
        
    return answer