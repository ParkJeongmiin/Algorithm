import sys

"""
N : 빌딩 수 <= 50

1. 빌딩 차례대로 순회
2. 자기 자신 제외하고 차례대로 직선 방적식 계산
3. 사이에 있는 빌딩 순회
3.1 사이에 빌딩 중 하나라도 직선보다 높이가 크면 - 비교 대상은 no count
3.2 전부 빌딩 보다 작으면(미만) - answer[목표 빌딩] += 1

시간 복잡도 : O(N * N-1 * N-1) ~= O(N^3) = 125,000
=> 완전 탐색 가능으로 판단
"""

# ----- input -----
input = sys.stdin.readline
N = int(input())
buildings = list(map(int, input().split()))

# ----- code -----
# initial settings
answer = 0

for i in range(N):  # target building idx
    count = 0

    for j in range(N):  # comapre building idx
        # 자기 자신 제외
        if i == j:
            continue

        slope = (buildings[j] - buildings[i]) / (j - i)

        visiable = True

        # 두 건물 사이의 idx
        # min(i, j) + 1 부터 max(j) 까지
        for x in range(min(i, j) + 1, max(i, j)):
            f_x = slope * (x - i) + buildings[i]

            if buildings[x] >= f_x:
                visiable = False
                break

        if visiable:
            count += 1

    answer = max(answer, count)

print(answer)
