import sys
from collections import deque


# ----- input -----
input = sys.stdin.readline
N, L, R = map(int, input().split())
maps = [list(map(int, input().split())) for _ in range(N)]

# ----- code -----
# initial settings
answer = 0
dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]


# bfs 정의
def bfs(r, c, visited):
    queue = deque([(r, c)])
    visited[r][c] = True

    groups = [(r, c)]  # 연합에 속한 나라들의 좌표 리스트
    counts = maps[r][c]  # 연합의 총 인구수

    while queue:
        y, x = queue.popleft()

        for i in range(4):
            ny, nx = y + dy[i], x + dx[i]

            # 범위 내에 있고, 아직 방문하지 않았다면
            if 0 <= nx < N and 0 <= ny < N and not visited[ny][nx]:
                # 국경선을 공유하는 두 나라의 인구 차이 계산
                diff = abs(maps[y][x] - maps[ny][nx])

                # 인구 차이가 L 이상 R 이하인 경우 (국경선 오픈)
                if L <= diff <= R:
                    visited[ny][nx] = True
                    queue.append((ny, nx))
                    groups.append((ny, nx))
                    counts += maps[ny][nx]

    return groups, counts


# main
while True:
    visited = [[False] * N for _ in range(N)]
    moved_flag = False  # 인구 이동 확인 flag

    # 모든 좌표 순회, 연합 시작점 탐색
    for r in range(N):
        for c in range(N):
            if not visited[r][c]:
                groups, counts = bfs(r, c, visited)

                # 연합에 속한 나라가 2개 이상인 경우
                # 인구 이동 발생
                if len(groups) > 1:
                    moved_flag = True
                    new_counts = counts // len(groups)

                    for y, x in groups:
                        maps[y][x] = new_counts

    # 모든 좌표를 돌았는데 인구 이동이 없었다면 과정 종료
    if not moved_flag:
        break

    answer += 1


print(answer)
