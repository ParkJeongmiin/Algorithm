from collections import defaultdict, Counter

def solution(topping):
    answer = 0
    
    # old = defaultdict(int)
    old = set()
    young = Counter(topping)
    
    for top in topping:
        old.add(top)
        young[top] -= 1
        
        if young[top] <= 0:
            del young[top]
            
        if len(old) == len(young):
            answer += 1
    
    return answer