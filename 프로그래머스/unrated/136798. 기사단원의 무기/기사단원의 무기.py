"""
1. 번호별 약수의 개수를 구한다.
2. (for) idx in range(len(dict))
    1) dict[idx] >= limit:
        True : dict[idx] = power
3. sum(dict.values())
"""       

def solution(number, limit, power):
    answer = 0
    weight_list = []
    
    for num in range(1, number + 1):
        count = 0
        
        for divid in range(1, int(num ** (1/2)) + 1):
            if num % divid == 0:
                count += 2
                if num/divid == divid:
                    count -= 1
        
        weight_list.append(count)
        
    for idx in range(len(weight_list)):
        if weight_list[idx] > limit:
            weight_list[idx] = power
            
    answer = sum(weight_list)
    
    return answer