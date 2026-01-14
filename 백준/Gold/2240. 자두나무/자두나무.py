import sys


"""
T : 자두가 떨어지는 총 시간
W : 최대 이동 횟수

# DP 테이블 정의를 위해 변하는 값 분석
- 시간(0 ~ T)
- 이동 횟수(0 ~ W)
따라서, dp[t][w]로 't초까지 w번 움직였을 때, 자두의 최대 개수'

# 현재 나무 위치 파악
- 짝수 번 이동하면 1번 나무(w % 2 == 0)
- 홀수 번 이동하면 2번 나무(w % 2 == 1)

# 점화식 정의
dp[t][w]가 되려면 [t-1]초의 상태는 '가만히 있었던 경우'와 '방금 움직인 경우'만 존재
- 가만히 있었던 경우 = [t-1]초에 이미 w번 움직인 경우 = dp[t-1][w]
- 방금 움직인 경우 = [t-1]초에 [w-1]번 움직인 경우 = dp[t-1][w-1]
따라서, 이 두 경우 중 큰 값과 현재 위치에서 잡을 수 있는지 여부를 더해 저장
dp[t][w] = max(dp[t-1][w], dp[t-1][w-1]) + catch(0 or 1)

+) w=0인 경우에는 이전에 움직인 경우가 없기 때문에 dp[t-1][0]으로만 계산
"""

# ----- input -----
input = sys.stdin.readline
T, W = map(int, input().split())

# ----- code -----
fruits = [0] + [int(input()) for _ in range(T)]
dp = [[0 for _ in range(W + 1)] for _ in range(T + 1)]

for t in range(1, T + 1):
    target = fruits[t]

    # 해당 시간에서 움직임 별 결과 계산
    for w in range(W + 1):
        cur_location = (w % 2) + 1  # 현재 나무 위치 계산

        # 현재 위치와 비교해 과일 섭취 성공 여부 판단
        catch = 1 if cur_location == target else 0

        if w == 0:
            dp[t][w] = dp[t - 1][w] + catch
        else:
            dp[t][w] = max(dp[t - 1][w], dp[t - 1][w - 1]) + catch

print(max(dp[T]))
