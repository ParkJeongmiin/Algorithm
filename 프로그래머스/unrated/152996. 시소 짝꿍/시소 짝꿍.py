from collections import Counter

def solution(weights):
    answer = 0
    
    counter = Counter(weights)
    weights = set(weights)
    
    # 무게비가 1:1인 경우
    for weight, person in counter.items():
        if person >= 2:
            answer += person * (person - 1) // 2
            
    # 무게비가 3/2, 2, 4/3 인 경우
    for w in weights:
        if w * 2/3 in weights:
            answer += counter[w * 2/3] * counter[w]
        
        if w * 2/4 in weights:
            answer += counter[w * 2/4] * counter[w]
        
        if w * 4/3 in weights:
            answer += counter[w * 4/3] * counter[w]
    
    return answer