from collections import deque


def cal_size(i, j, land, visited, result):
    """
    하나의 덩어리 크기를 계산하는 함수
    """
    size = 1
    queue = deque()
    queue.append([i, j])
    visited[i][j] = True
    
    min_x, max_x = j, j
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        y, x = queue.popleft()
        
        min_x = min(min_x, x)
        max_x = max(max_x, x)
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < len(land) and 0 <= nx < len(land[0]):
                if land[ny][nx] and not visited[ny][nx]:
                        visited[ny][nx] = True
                        queue.append((ny, nx))
                        size += 1
                        
    for i in range(min_x, max_x + 1):
        result[i] += size
    
    return result
    


def solution(land):
    n, m = len(land), len(land[0])
    result = [0 for _ in range(m)]
    visited = [[False] * m for _ in range(n)]
    
    for j in range(m):
        total = 0
        
        for i in range(n):
            if land[i][j] and not visited[i][j]:
                cal_size(i, j, land, visited, result)
                
    return max(result)
