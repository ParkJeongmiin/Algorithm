from collections import deque

''' 그래프 생성 '''
m, n = map(int, input().split())
graph = []
queue = deque([])

for i in range(n):
    graph.append(list(map(int, input().split())))
    
    for j in range(m):            # 동시에 시작되는 경우 대비
        if graph[i][j] == 1:
            queue.append([i, j])
            
''' BFS 함수 정의 '''
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

def bfs():
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < m and graph[ny][nx] == 0:
                queue.append([ny, nx])
                graph[ny][nx] = graph[y][x] + 1
                
''' 결과 출력 '''
bfs()

answer = 0
for row in graph:
    for col in row:
        if col == 0:
            print(-1)
            exit(0)
    answer = max(answer, max(row))
print(answer - 1)