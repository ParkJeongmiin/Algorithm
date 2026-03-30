import sys

# ----- input -----
input = sys.stdin.readline
M, N, H = map(int, input().split())

# ----- code -----
day = 0
non_perfect = 0
cur_list = []
dy = [0, 0, -1, 1, 0, 0]
dx = [0, 0, 0, 0, 1, -1]
dh = [-1, 1, 0, 0, 0, 0]

maps = [[[0] * M for _ in range(N)] for _ in range(H)]

for i in range(H):
    for j in range(N):
        row = list(map(int, input().split()))

        for k in range(M):
            maps[i][j][k] = row[k]

            if row[k] == 1:  # 익은 토마토 좌표 저장, 방문 처리(중복 계산 방지)
                cur_list.append((i, j, k))
                maps[i][j][k] = 2
            elif row[k] == 0:  # 익지 않은 토마토 개수 update
                non_perfect += 1

# 시작부터 다 익은 경우 종료.
if non_perfect == 0:
    print(0)
    sys.exit()

# 시뮬레이션
next_list = []
while cur_list:
    if non_perfect == 0:  # 모든 토마토가 익었을 경우 종료
        break

    day += 1
    for h, y, x in cur_list:  # 6 방향 확인
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nh = h + dh[i]

            if 0 <= ny < N and 0 <= nx < M and 0 <= nh < H:  # 범위 내 칸 조회 확인
                if maps[nh][ny][nx] == 0:  # 익지 않은 토마토가 있는 칸인 경우
                    maps[nh][ny][nx] = 2  # 방문 처리로 같은 날 중복 계산 방지
                    next_list.append((nh, ny, nx))
                    non_perfect -= 1

    cur_list = next_list
    next_list = []

if non_perfect == 0:
    print(day)
else:
    print(-1)
