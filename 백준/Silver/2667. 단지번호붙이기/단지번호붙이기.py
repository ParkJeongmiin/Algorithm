from collections import deque

n = int(input())
maps = []
for _ in range(n):
    maps.append(list(map(int, input())))
    
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

# BFS 함수
def bfs(maps, col, row):
    queue = deque()
    queue.append([col, row])
    maps[col][row] = 0
    count = 1
    
    while queue:
        y, x = queue.popleft()
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < n and 0 <= nx < n and maps[ny][nx] == 1:
                maps[ny][nx] = 0
                queue.append([ny, nx])
                count += 1
                
    return count

# 시작할 위치 찾으면 bfs 돌리기
answer = []
for col in range(n):
    for row in range(n):
        if maps[col][row] == 1:
            count = bfs(maps, col, row)
            answer.append(count)

# 정답 출력
answer.sort()
print(len(answer))
for num in answer:
    print(num)