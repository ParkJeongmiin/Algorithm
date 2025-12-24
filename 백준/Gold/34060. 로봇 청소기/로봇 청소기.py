import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline

N = int(input())
ys = [int(input()) - 1 for _ in range(N)]

# ----- code -----
# 최솟값 알고리즘
maps = set()
cur_x, last_y = 0, -1
for y in ys:
    if y <= last_y:  # greedy 한 줄에 최대한 많이 위치시키기
        cur_x += 1

    maps.add((y, cur_x))
    last_y = y

visited = set()
min_answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

for coord in maps:
    # 이미 방문 처리 된 곳은 넘어가기
    if coord in visited:
        continue

    # 새로운 영역은 정답 +1
    min_answer += 1
    visited.add(coord)  # 방문 처리
    queue = deque([coord])

    # 주변 영역 탐색
    while queue:
        cy, cx = queue.popleft()

        for i in range(4):
            ny, nx = cy + dy[i], cx + dx[i]

            # 오염이 있고, 새로운 곳이라면 (방문처리), (주변 영역 큐에 넣기)
            if (ny, nx) in maps and (ny, nx) not in visited:
                visited.add((ny, nx))
                queue.append((ny, nx))

print(min_answer)
print(N)
