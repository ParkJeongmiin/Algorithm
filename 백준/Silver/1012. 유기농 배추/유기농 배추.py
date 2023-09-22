from collections import deque

# BFS 함수 정의
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


def bfs(maps, col, row):
    queue = deque()
    queue.append([col, row])
    maps[col][row] = 0

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < n and 0 <= nx < m and maps[ny][nx] == 1:
                queue.append([ny, nx])
                maps[ny][nx] = 0

# 결과 계산
t = int(input())

for _ in range(t):
    m, n, k = map(int, input().split())
    count = 0

    # 지도 생성
    maps = [[0] * m for _ in range(n)]
    for _ in range(k):
        r, c = map(int, input().split())
        maps[c][r] = 1

    for col in range(n):
        for row in range(m):
            if maps[col][row] == 1:
                bfs(maps, col, row)
                count += 1

    print(count)