import sys

# ----- input -----
input = sys.stdin.readline
N = int(input())

# ----- code -----
maps = [list(map(int, input().split())) for _ in range(N)]

# (r, c, dir) (dir 0: 가로, 1: 세로:)
dp = [[[0] * 3 for _ in range(N)] for _ in range(N)]
dp[0][1][0] = 1

for r in range(N):
    for c in range(N):
        if maps[r][c]:
            continue

        # 현재 상태가 가로라면 [r][c][0]
        ## [r][c - 1]이 가로 혹은 대각이었다.
        ## c - 1이 0보다는 커야 범위 안이다.
        if c - 1 >= 0:
            dp[r][c][0] += dp[r][c - 1][0]
            dp[r][c][0] += dp[r][c - 1][2]

        # 현재 상태가 세로라면 [r][c][1]
        ## [r - 1][c]이 세로 혹은 대각이었다.
        ## r - 1이 0보다는 커야 범위 안이다.
        if r - 1 >= 0:
            dp[r][c][1] += dp[r - 1][c][1]
            dp[r][c][1] += dp[r - 1][c][2]

        # 현재 상태가 대각이라면 [r][c][2]
        ## [r - 1][c - 1]이 가로, 세로, 대각 중 하나였다.
        ## r - 1, c - 1이 모두 0이상이어야 범위 안이다.
        ## 주변 4칸에 벽이 하나도 없어야 한다.
        if c - 1 >= 0 and r - 1 >= 0:
            if maps[r - 1][c] == 0 and maps[r][c - 1] == 0:
                dp[r][c][2] += dp[r - 1][c - 1][0]
                dp[r][c][2] += dp[r - 1][c - 1][1]
                dp[r][c][2] += dp[r - 1][c - 1][2]

print(sum(dp[-1][-1]))
