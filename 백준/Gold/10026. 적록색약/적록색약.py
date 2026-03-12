import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline
N = int(input())

# ----- code -----
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]
maps = [list(input().strip()) for _ in range(N)]


def bfs(y, x):
    queue = deque([(y, x)])
    visited[y][x] = True
    cur_color = maps[y][x]

    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny = cy + dy[i]
            nx = cx + dx[i]

            if 0 <= ny < N and 0 <= nx < N and not visited[ny][nx]:
                if maps[ny][nx] == cur_color:
                    queue.append((ny, nx))
                    visited[ny][nx] = True


# 1. 정상인 판단
visited = [[False] * N for _ in range(N)]
normal_count = 0

for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x)
            normal_count += 1

# 2. 적록 색약인 판단
for y in range(N):
    for x in range(N):
        if maps[y][x] == "G":
            maps[y][x] = "R"

visited = [[False] * N for _ in range(N)]
blind_count = 0
for y in range(N):
    for x in range(N):
        if not visited[y][x]:
            bfs(y, x)
            blind_count += 1

print(f"{normal_count} {blind_count}")
