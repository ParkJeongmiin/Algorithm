from collections import deque

def bfs(src, dest, maps):
    height = len(maps)
    width = len(maps[0])
    
    # 시작 지점 찾아서 큐에 삽입, 방문 처리
    queue = deque()
    visited = [[False] * width for _ in range(height)]
    
    for row in range(height):
        for col in range(width):
            if maps[row][col] == src:
                queue.append([row, col, 0])
                visited[row][col] = True
                
    # bfs 탐색
    dy = [-1, 1, 0, 0]
    dx = [0, 0, -1, 1]
    
    while queue:
        y, x, cost = queue.popleft()
        
        if maps[y][x] == dest:
            return cost
        
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]
            
            if 0 <= ny < height and 0 <= nx < width and maps[ny][nx] != 'X':
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    queue.append([ny, nx, cost + 1])
                    
    return -1
                

def solution(maps):
    answer = 0
    
    cost_1 = bfs('S', 'L', maps)
    cost_2 = bfs('L', 'E', maps)
    
    if cost_1 == -1 or cost_2 == -1:
        return -1
    else:
        return cost_1 + cost_2

'''
출발지점 -> 레버 -> 출구
한 칸에 1초 걸린다. return 최소시간
* 탈출할 수 없다면  return -1

* 레버를 당기지 않고 출구를 지나는 것은 가능

같은 칸을 여러 번 지날 수 있다.
s(출발), e(출구), l(레버), x(벽), o(통로)

최단거리 구하기 -> BFS
1. 미로의 크기, 시작점, 레버위치, 도착점 구하기
2. bfs로 레버까지 최단거리 구하기
3. 방문한 노드 전부 초기화
4. 레버에서 출구까지 최단거리 구하기
'''