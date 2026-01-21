import sys

"""
N : 빌딩 수 <= 50

# 오른쪽 빌딩과 비교
- target, compare 빌딩의 기울기 계산
- 지금까지 최대 기울기 보다 큰 경우에만 count += 1
- 당시 최댓값보다 작은 경우는 가린다.

# 왼쪽 빌딩과 비교
- target, compare 빌딩의 기울기 계산
- 그 당시 최소 기울기보다 작은 경우에만 count += 1

시간 복잡도
중간에 빌딩들을 다시 순회하지 않아도 되기 때문에 O(N^2)
"""

# ----- input -----
input = sys.stdin.readline
N = int(input())
buildings = list(map(int, input().split()))

# ----- code -----
# initial settings
INF = sys.maxsize
answer = 0

for i in range(N):
    count = 0

    # 오른쪽 빌딩들 비교
    max_slope = -INF
    for j in range(i + 1, N):
        slope = (buildings[j] - buildings[i]) / (j - i)

        if max_slope < slope:
            count += 1
            max_slope = slope

    # 왼쪽 빌딩들 비교
    min_slope = INF
    for j in range(i - 1, -1, -1):
        slope = (buildings[j] - buildings[i]) / (j - i)

        if slope < min_slope:
            count += 1
            min_slope = slope

    answer = max(answer, count)

print(answer)
