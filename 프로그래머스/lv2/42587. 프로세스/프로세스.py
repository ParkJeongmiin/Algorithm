from collections import deque

def solution(priorities, location):
    answer = 0
    priorities = deque(priorities)
    location -= len(priorities)
    
    while True:
        max_idx = priorities.index(max(priorities))
        
        if max_idx == location + len(priorities):
            answer += 1
            break
            
        priorities.rotate(-max_idx)
        
        location -= max_idx
        if location < -len(priorities):
            location += len(priorities)
        
        priorities.popleft()
        answer += 1
        
    return answer