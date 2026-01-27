import sys

# ----- input -----
input = sys.stdin.readline
N, K, P, X = map(int, input().split())

# ----- code -----
# initial settings
answer = 0
segments = [
    "1111110",  # 0
    "0000110",  # 1
    "1011011",  # 2
    "1001111",  # 3
    "0100111",  # 4
    "1101101",  # 5
    "1111101",  # 6
    "1000110",  # 7
    "1111111",  # 8
    "1101111",  # 9
]

costs = [[0] * 10 for _ in range(10)]  # 숫자별 변환 비용 테이블
for i in range(10):  # 숫자별 변환 비용 계산
    for j in range(10):
        diff = 0

        for idx in range(7):
            if segments[i][idx] != segments[j][idx]:
                diff += 1

        costs[i][j] = diff

current_str = str(X).zfill(K)  # 현재 층(X)를  K 자리의 문자열로 표현

# 전체 층(target)을 순회하면서 가능한 경우의 수 탐색
for target in range(1, N + 1):
    target_str = str(target).zfill(K)
    needed_flips = 0

    # X와 target 사이 변환 시 비용 계산
    for idx in range(K):
        cur_num, target_num = int(current_str[idx]), int(target_str[idx])
        needed_flips += costs[cur_num][target_num]

        if needed_flips > P:
            break

    if 1 <= needed_flips <= P:
        answer += 1

print(answer)
