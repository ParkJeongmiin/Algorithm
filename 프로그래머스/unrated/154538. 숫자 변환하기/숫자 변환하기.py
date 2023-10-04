from collections import deque

def solution(x, y, n):
    
    answer = 0
    
    queue = deque()
    queue.append([x, 0])
    
    visited = set()
    
    while queue:
        parent, depth = queue.popleft()
        
        if parent == y:
            return depth
        
        for child in [parent + n, parent * 2, parent * 3]:
            
            if child <= y and not child in visited:
                visited.add(child)
                queue.append([child, depth + 1])

    return -1

