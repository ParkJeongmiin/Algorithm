'''
bfs
1. 지도를 전부 순회하면서 시작할 수 있는 위치(= [해당 위치가 X가 아니고] and [방문하지 않은 곳])를 찾는다.
2. 시작할 위치를 찾았다면 bfs 시작
    1) 탐색하면서 해당 위치의 값을 더해간다.
    2) 탐색한 곳은 방문처리하고 다음 인접한 곳 탐색
    3) 탐색이 끝나면 탐색하는 동안 더한 값을 반환
'''
from collections import deque

def bfs(y, x, maps, visited):
    
    cost = int(maps[y][x])
    height = len(maps)
    width = len(maps[0])
    
    queue = deque()
    queue.append([y, x])
    
    visited[y][x] = True
    
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < height and 0 <= nx < width and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx])
                    cost += int(maps[ny][nx])
    
    return cost
    
def solution(maps):
    answer = []
    
    height = len(maps)
    width = len(maps[0])
    
    # 방문 처리 관리
    visited = [[False] * width for _ in range(height)]
    
    # 시작점 찾기
    for i in range(height):
        for j in range(width):
            if maps[i][j] != 'X' and visited[i][j] == False:
                answer.append(bfs(i, j, maps, visited))
    
    answer.sort()
    
    if len(answer) != 0:
        return answer
    else:
        return [-1]