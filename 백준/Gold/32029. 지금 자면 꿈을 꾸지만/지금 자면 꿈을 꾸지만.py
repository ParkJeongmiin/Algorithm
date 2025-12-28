import sys

"""
1. 마감 기한 빠른 순으로 정렬 asc   N log N
2. 모든 X에 대해서 확인
3. 잠을 안자는 경우(k = X)와 과제를 k 개 끝내고 자는 경우로 나눌 수 있다.

=> X와 k에 의한 answer

X[0:A-1]와 k[0:N] 설정
1. k개 과제 수행 -> cur_time_k(A_i) <= T_i : ans += 1 : continue
2. 잠자기 cur_time += B*X, A = A-X
3. 남은 과제 수행 -> cur_time_k(A_i) <= T_i : ans += 1 : continue
"""
# ----- input -----
input = sys.stdin.readline

N, A, B = map(int, input().split())
T_list = list(map(int, input().split()))

# ----- code -----
T_list.sort()
answer = 0

# 1. 가능한 모든 X의 경우 확인 [0 : A-1]
for X in range(A):
    sleep_time = B * X
    reduced_A = A - X

    # 2. 자기 전 수행하는 과제 개수 설정
    # k: k 번째 과제(idx = k-1)를 마치고 잠을 잔다.
    for k in range(N + 1):
        cur_time = 0
        count = 0

        # 모든 과제에 대한 시뮬레이션
        # i: 해당 과제 가능 여부 판단 시 사용
        # k: 잠자는 타이밍 확인시 사용
        for i in range(N):
            # 설정된 잠자는 시간
            if i == k:
                cur_time += sleep_time

            # 과제 수행 비용 설정
            if i < k:
                cost = A
            else:
                cost = reduced_A

            # 과제 기한과 비교해 수행 가능 여부 판단
            if cur_time + cost <= T_list[i]:
                cur_time += cost
                count += 1

        answer = max(answer, count)

print(answer)
