import sys


# ----- input -----
input = sys.stdin.readline

M, N = map(int, input().split())

maps = []
for _ in range(M):
    maps.append(list(map(int, input().split())))

r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1 - 1, c1 - 1, r2 - 1, c2 - 1

# ----- code -----
EMPTY = -2
VIBRANIUM = -1
BOMB = 0

# Initial Swap
maps[r1][c1], maps[r2][c2] = maps[r2][c2], maps[r1][c1]

answer = 0
active_bombs = set()

while True:
    # ============
    # Stage 1 구현
    # ============
    while True:
        to_remove = set()

        # 가로 매치 확인
        for y in range(M):
            for x in range(N - 2):
                val = maps[y][x]
                if val > 0:
                    if maps[y][x + 1] == val and maps[y][x + 2] == val:
                        c = 0
                        while x + c < N and maps[y][x + c] == val:
                            to_remove.add((y, x + c))
                            c += 1

        # 세로 매치 확인
        for x in range(N):
            for y in range(M - 2):
                val = maps[y][x]
                if val > 0:
                    if maps[y + 1][x] == val and maps[y + 2][x] == val:
                        c = 0
                        while y + c < M and maps[y + c][x] == val:
                            to_remove.add((y + c, x))
                            c += 1

        if not to_remove:  # 지울 보석이 없는 경우 Stage 2로 이동
            break

        # 3-match 보석 제거
        for y, x in to_remove:
            if maps[y][x] != EMPTY:
                maps[y][x] = EMPTY
                answer += 1

        # 중력 적용
        new_active_bombs = set()
        for x in range(N):
            col_items = []  # 현재 열의 상태 저장 (값, 이전 행 번호, 활성 여부)

            for y in range(M):
                val = maps[y][x]
                if val != EMPTY:
                    is_active = (y, x) in active_bombs
                    col_items.append({"val": val, "old_r": y, "active": is_active})

            # 해당 열 비우기
            for y in range(M):
                maps[y][x] = EMPTY

            # 바닥부터 채우기
            current_y = M - 1
            for item in reversed(col_items):
                val = item["val"]
                maps[current_y][x] = val

                # 폭탄 활성화 여부 확인
                if val == BOMB:
                    if item["active"] or (item["old_r"] != current_y):
                        new_active_bombs.add((current_y, x))

                current_y -= 1

        active_bombs = new_active_bombs

    # ============
    # Stage 2 구현
    # ============
    # 활성화된 폭탄이 하나도 없으면 전체 시퀀스 종료
    if not active_bombs:
        break

    explosion_targets = set()
    direction = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 상하좌우

    for by, bx in active_bombs:
        explosion_targets.add((by, bx))

        for dy, dx in direction:
            ny, nx = by + dy, bx + dx

            while 0 <= ny < M and 0 <= nx < N:
                if maps[ny][nx] == VIBRANIUM:  # 비브라늄을 만나면 해당 방향 폭발 종료
                    break

                # 한 방향으로 계속 나아가기
                explosion_targets.add((ny, nx))
                ny += dy
                nx += dx

    active_bombs.clear()

    # 폭발된 좌표들 빈자리로 표시
    for y, x in explosion_targets:
        if maps[y][x] != EMPTY:
            maps[y][x] = EMPTY
            answer += 1

    # 중력 적용
    new_active_bombs = set()
    for x in range(N):
        col_items = []

        for y in range(M):
            val = maps[y][x]

            if val != EMPTY:
                col_items.append({"val": val, "old_y": y})

        # 해당 열 비우기
        for y in range(M):
            maps[y][x] = EMPTY

        # 바닥부터 채우기
        current_y = M - 1
        for item in reversed(col_items):
            val = item["val"]
            maps[current_y][x] = val

            if val == BOMB:
                if item["old_y"] != current_y:
                    new_active_bombs.add((current_y, x))

            current_y -= 1

    active_bombs = new_active_bombs

print(answer)
