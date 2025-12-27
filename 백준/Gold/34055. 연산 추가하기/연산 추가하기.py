import sys
from bisect import bisect_left

"""
N = 0 인 경우
1 <= S <= S+T-1 <= H 에서 S의 개수를 구하는 문제
S = H - T + 1 개

N개 구간의 합집합을 제외한 영역 별로 계산해야한다.
[a, b] 구간이라면 (b - a + 1) - T + 1 이 해당 구간의 정답이 된다.
만약 해당 구간이 Q 보다 작으면 진행하지 않는다.
전체 구간에 대해서 진행하면 O(QN) -> 시간초과

=> 가능한 구간의 길이를 계산해 저장한 다음 사용

# 기존 연산 전처리
1. 기존 연산(N)의 연산 구간 정렬 asc    N log N
2. 기존 연산들의 합집합 계산            N
3. 빈 구간의 길이 계산, 정렬            N log N
=> O(N log N)

# 추가 연산 위치 계산
1. 이분 탐색을 통해 들어갈 수 있는 구간 찾기    log N
2. l_i - Q + 1 계산
3. Q 번 반복
=> O(Q log N)

해당 방법의 시간 복잡도는 O((N+Q)logN)
"""
# ----- input -----
input = sys.stdin.readline

N, H = map(int, input().split())
models = [list(map(int, input().split())) for _ in range(N)]
Q = int(input())

# ----- code -----
# 전처리
models.sort(key=lambda x: x[0])  # 시작 위치 기준 asc 정렬

merged = []
if N > 0:
    cur_start, cur_end = models[0]

    for i in range(1, N):
        next_start, next_end = models[i]

        if next_start <= cur_end + 1:
            # 겹치거나 연결된 경우는 누적 경우 -> 확장
            cur_end = max(cur_end, next_end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = next_start, next_end

    merged.append((cur_start, cur_end))

# 빈 구간 길이 계산
empty_lengths = []
cur_time = 1
for start, end in merged:
    if cur_time < start:  # 현재 시간이 연산 시작 보다 앞 -> 빈 공간
        empty_lengths.append(start - cur_time)

    cur_time = max(cur_time, end + 1)  # 연산 종료 시점으로 이동

if cur_time <= H:  # 사이클 끝까지 확인
    empty_lengths.append(H - cur_time + 1)

empty_lengths.sort()  # 이분 탐색을 위한 asc 정렬

# 누적합 계산
len_counts = len(empty_lengths)
prefix_sum = [0] * (len_counts + 1)
for i in range(len_counts):
    prefix_sum[i + 1] = prefix_sum[i] + empty_lengths[i]

# 쿼리 처리
for _ in range(Q):
    T = int(input())

    idx = bisect_left(empty_lengths, T)  # 추가 연산 크기를 만족하는 구간의 idx 찾기
    count = len_counts - idx  # 추가 연산이 들어갈 수 있는 구간 개수
    valid_lengths = prefix_sum[len_counts] - prefix_sum[idx]  # 유효한 구간 전체 길이

    # Sum(L_i - T + 1) -> Sum(L_i) - Sum(T - 1) 분리
    # (유효한 구간 전체 길이) + (가능한 구간 개수) * (T - 1)
    answer = valid_lengths - count * (T - 1)

    print(answer, end="\n")
