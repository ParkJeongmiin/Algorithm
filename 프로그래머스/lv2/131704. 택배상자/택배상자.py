from collections import deque

def solution(order):
    answer = 0
    
    order = deque(order)
    side = []
    
    for i in range(1, len(order) + 1):
        side.append(i)
        
        while side and side[-1] == order[0]:
            side.pop()
            order.popleft()
            answer += 1
    
    return answer
