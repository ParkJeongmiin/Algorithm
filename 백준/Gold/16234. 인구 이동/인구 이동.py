import sys
from collections import deque


# ----- input -----
input = sys.stdin.readline
N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# ----- code -----
# initial settings
answer = 0
candidates = deque([(r, c) for r in range(N) for c in range(N)])
visited = [[-1] * N for _ in range(N)]
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# bfs 정의
def bfs(r, c, visited):
    queue = deque([(r, c)])
    visited[r][c] = answer  # 방문처리 memoization - 메모리 절약

    groups = [(r, c)]
    total_counts = maps[r][c]

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            if 0 <= ny < N and 0 <= nx < N and visited[ny][nx] != answer:
                if L <= abs(maps[y][x] - maps[ny][nx]) <= R:
                    visited[ny][nx] = answer
                    queue.append((ny, nx))
                    groups.append((ny, nx))
                    total_counts += maps[ny][nx]

    return groups, total_counts


# main
while True:
    next_candidates = set()  # 다음 날 확인해 볼 좌표들
    moved_flag = False

    for _ in range(len(candidates)):
        r, c = candidates.popleft()

        if visited[r][c] == answer:  # 탐색하는 당일에 방문한 곳이면 넘어가기
            continue

        # BFS 로직 시작
        groups, total_counts = bfs(r, c, visited)

        # 연합에 속한 나라가 2개 이상인 경우
        # 인구 이동 발생
        if len(groups) > 1:
            moved_flag = True
            new_counts = total_counts // len(groups)

            for y, x in groups:
                maps[y][x] = new_counts

                # 탐색 범위 제한 - 변화된 나라와 주변국만 저장
                next_candidates.add((y, x))
                for i in range(4):
                    ny, nx = y + dy[i], x + dx[i]
                    if 0 <= ny < N and 0 <= nx < N:
                        next_candidates.add((ny, nx))

    if not moved_flag:
        break

    answer += 1
    candidates = deque(list(next_candidates))

print(answer)
