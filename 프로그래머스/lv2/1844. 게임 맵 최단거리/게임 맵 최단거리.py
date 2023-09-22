from collections import deque

def solution(maps):
    
    col = len(maps)
    row = len(maps[0])
    
    queue = deque()
    queue.append([0, 0])
    visited = [[False] * row for _ in range(col)]
    visited[0][0] = True        # 시작위치 방문처리
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:

        y, x = queue.popleft()      # 현재 위치
        
        for i in range(4):          # 인접한 노드들 탐색
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < col and 0 <= nx < row and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                    maps[ny][nx] = maps[y][x] + 1
                    
    if maps[-1][-1] != 1:
        return maps[-1][-1]
    else:
        return -1