import sys


"""
N <= 2*10^5, C <= 2*10^5
x_i <= 10^9

"가장 인접한 두 공유기 사이의 거리를 최대로 한다"
= 최솟값의 최대값 계산
= 이분 탐색

문제 질문을 "C개 설치할 때 거리의 최댓값"에서
"가장 인접한 거리를 D로 했을 때, 설치할 수 있는 공유기 개수는?"으로 변경

1. 첫 번째 집에 공유기 무조건 설치한다고 가정
2. 직전 설치 집과 D 이상 떨어진 집에만 설치 - 설치된 공유기 수 계산
3. D는 이분 탐색 : 1 ~ (처음, 끝 집의 거리)에서 탐색

# 시간 복잡도
1. 정렬 : O(N log N)
2. 이분 탐색 : log 10^9 ~= 30
3. 모든 집 순회 : O(N)
=> O(N log N + N log 30)
"""

# ----- input -----
input = sys.stdin.readline
N, C = map(int, input().split())
houses = [int(input()) for _ in range(N)]

# ----- code -----
# initial settings
houses.sort()

answer = 0
start, end = 1, (houses[-1] - houses[0])

while start <= end:
    mid = (start + end) // 2

    # 첫 번째 집 설치
    current_C = 1
    current_house = houses[0]

    # 집들 순회하면서 설치 여부 판단해 설치
    for i in range(1, N):
        if houses[i] - current_house >= mid:
            current_C += 1
            current_house = houses[i]

    # 정해진 C 보다 커진다면, 거리 키우기
    if current_C >= C:
        start = mid + 1
        answer = mid
    # 목표치를 채우지 못했다면, 거리 좁히기
    else:
        end = mid - 1

print(answer)