import sys

# ----- input -----
input = sys.stdin.readline

N, K = map(int, input().split())

cond = [[0, 0]]
for _ in range(N):
    w, v = map(int, input().split())
    cond.append([w, v])

# ----- code -----
# 현재 물건 무게를 바탕으로
# 이전의 물건의 무게와 계산
# dp[현재 물건][현재 가방 무게]
#   1. dp[이전 물건][현재 가방 무게]
#   2. (현재 물건 value) + dp[이전 물건][현재 가방 무게 - 현재 물건 무게]
#       -> 이전 상황에서 현재 물건이 들어갈 여유가 있는 상황의 무게 가져오기

dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]

for i in range(N + 1):
    for j in range(K + 1):
        w = cond[i][0]
        v = cond[i][1]

        if j < w:
            dp[i][j] = dp[i - 1][j]
        else:
            dp[i][j] = max(dp[i - 1][j], v + dp[i - 1][j - w])

print(dp[N][K])
