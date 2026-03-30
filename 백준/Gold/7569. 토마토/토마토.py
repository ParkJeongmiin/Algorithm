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

# maps 구성
maps = []
for h in range(H):
    layer = []

    for y in range(N):
        row = list(map(int, input().split()))

        for x, val in enumerate(row):  # 인덱스 접근 오버헤드 최소화
            if val == 1:
                cur_list.append((h, y, x))
            elif val == 0:
                non_perfect += 1

        layer.append(row)

    maps.append(layer)

# 시작부터 다 익은 경우 종료.
if non_perfect == 0:
    print(0)
    sys.exit()

# 시뮬레이션
while cur_list:
    if non_perfect == 0:  # 모든 토마토가 익었을 경우 종료
        break

    day += 1
    next_list = []
    for h, y, x in cur_list:  # 6 방향 확인
        for i in range(6):
            ny = y + dy[i]
            nx = x + dx[i]
            nh = h + dh[i]

            if 0 <= ny < N and 0 <= nx < M and 0 <= nh < H:  # 범위 내 칸 조회 확인
                if maps[nh][ny][nx] == 0:  # 익지 않은 토마토가 있는 칸인 경우
                    maps[nh][ny][nx] = 1  # 방문 처리로 같은 날 중복 계산 방지
                    next_list.append((nh, ny, nx))
                    non_perfect -= 1

    cur_list = next_list

if non_perfect == 0:
    print(day)
else:
    print(-1)
