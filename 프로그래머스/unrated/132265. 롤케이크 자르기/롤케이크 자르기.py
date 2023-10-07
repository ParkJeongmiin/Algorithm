from collections import defaultdict, Counter

def solution(topping):
    answer = 0
    
    old = defaultdict(int)
    young = Counter(topping)
    
    for top in topping:
        old[top] += 1
        young[top] -= 1
        
        if young[top] <= 0:
            del young[top]
            
        if len(old) == len(young):
            answer += 1
    
    return answer