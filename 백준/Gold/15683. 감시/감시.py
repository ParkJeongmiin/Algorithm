import sys


"""
사각지대 최소 크기 = 0의 개수

CCTV 개수 별 경우의 수
CCTV : [1, 2, 3, 4, 5]
경우 : [4, 2, 4, 4, 1]

# 완전탐색
1. 전체 map 순회
    cctv 위치 + 유형 추출 
2. cctv 순회하면서 가능한 방향들로 모든 경우의 수 계산(DFS)
-> O(NM * C) = 8^2 * 4^8 = 4 * 10^6
"""

# ----- input -----
input = sys.stdin.readline
N, M = map(int, input().split())

# ----- code -----
# initial settings

dy = [-1, 0, 1, 0]  # 상, 우, 하, 좌
dx = [0, 1, 0, -1]

cctv_mode = [
    [],
    [[0], [1], [2], [3]],
    [[0, 2], [1, 3]],
    [[0, 1], [1, 2], [2, 3], [0, 3]],
    [[1, 2, 3], [0, 2, 3], [0, 1, 3], [0, 1, 2]],
    [[0, 1, 2, 3]],
]

# maps 입력 + cctv 타입, 위치 추출
maps = []
cctv_info = []
for y in range(N):
    row = list(map(int, input().split()))
    maps.append(row)

    for x in range(M):
        if 1 <= row[x] <= 5:
            cctv_info.append((row[x], y, x))


# dfs 정의
def dfs(number, current_maps):
    global answer

    # 모든 CCTV를 다 확인했을 때 - 현재 map의 0 개수 계산
    if number == len(cctv_info):
        count = 0
        for row in current_maps:
            count += row.count(0)
        answer = min(answer, count)
        return

    # 현재 number에 해당하는 cctv에서 가능한 방향 모두 계산
    mode, y, x = cctv_info[number]  # cctv_mode, y, x 조회

    for directions in cctv_mode[mode]:  # 여러 경우의 수 중에 하나로 계산
        temp_board = [row[:] for row in current_maps]

        # 하나의 경우의 수에서 map에 저장
        for d in directions:
            ny, nx = y, x  # 시작 지점 지정

            while True:
                ny += dy[d]
                nx += dx[d]

                # 범위 밖 and 벽(6) 이면 중지
                if not (0 <= ny < N and 0 <= nx < M) or temp_board[ny][nx] == 6:
                    break

                # 빈 공간이면 7 표시, 다른 cctv가 있는 경우는 그냥 넘어가기
                if temp_board[ny][nx] == 0:
                    temp_board[ny][nx] = 7

        # 하나의 경우의 수에 대해 계산 후, 다음 cctv로 넘어가기
        dfs(number + 1, temp_board)


answer = 100
dfs(0, maps)
print(answer)
