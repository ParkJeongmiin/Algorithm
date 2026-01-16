import sys


"""
N <= 500
tree <= 10^6

그래프 탐색 + dynamic programming

1. dp[y][x] table : 해당 좌표에서 이동할 수 있는 최대 칸
2. dfs 정의
    1) 다음 칸(상, 하, 좌, 우) 조회
    2) maps[ny][nx] > maps[y][x] 인 경우 dfs(ny, nx) 재귀 호출
    3) dp[y][x] = max(dp[y][x], 1 + dfs(ny, nx))로 저장
3. 모든 좌표에 대해서 탐색
"""

# ----- input -----
sys.setrecursionlimit(10**6)
input = sys.stdin.readline
N = int(input())


# ----- code -----
# initial settings
maps = [list(map(int, input().split())) for _ in range(N)]
dp = [[0 for _ in range(N)] for _ in range(N)]
dy, dx = [-1, 1, 0, 0], [0, 0, -1, 1]


# dfs 로직 설계
def dfs(y, x):
    # 이미 계산됐던 위치면 그대로 출력
    if dp[y][x] != 0:
        return dp[y][x]

    dp[y][x] = 1  # 시작 위치에서 자기 자신 포함한 1칸

    # 주변 위치 탐색
    for i in range(4):
        ny = y + dy[i]
        nx = x + dx[i]

        # 범위 내에 있고, 다음 칸의 숫자가 더 큰 경우 탐색 계속 진행
        if 0 <= ny < N and 0 <= nx < N:
            if maps[ny][nx] > maps[y][x]:
                dp[y][x] = max(dp[y][x], 1 + dfs(ny, nx))

    return dp[y][x]


# 모든 좌표에 대해 탐색
answer = 0
for y in range(N):
    for x in range(N):
        answer = max(answer, dfs(y, x))

print(answer)
