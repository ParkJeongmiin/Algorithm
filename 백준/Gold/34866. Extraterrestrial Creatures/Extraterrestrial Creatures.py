import sys


# 올림 (A / B) = (A + B - 1) / b
# 올림 (mid - init) / inc ==> ((mid - init) + inc - 1) / inc

# ----- input -----
input = sys.stdin.readline

N, X = map(int, input().split())

val_list = list(map(int, input().split()))
increase_list = list(map(int, input().split()))


# ----- code -----
def get_press_count(mid):
    # mid까지 각 개체가 도달하기 까지 누른 횟수 계산하는 함수
    total_cnt = 0
    for i in range(N):
        cnt = (mid - val_list[i] + increase_list[i] - 1) // increase_list[i]
        total_cnt += cnt

        if total_cnt > X:
            return total_cnt
    return total_cnt


low = 0
high = 2 * 10**18  # val + X * inc 최대 = 10^6 + 10^6 + 10^12 ~ 2 * 10^18
target_val = 0

while low <= high:
    mid = (low + high) // 2
    if get_press_count(mid) <= X:
        target_val = mid
        low = mid + 1
    else:
        high = mid - 1

cur_list = []
used_x = 0
for i in range(N):
    cnt = 0
    if val_list[i] < target_val:
        cnt = (target_val - val_list[i] + increase_list[i] - 1) // increase_list[i]

    val = val_list[i] + increase_list[i] * cnt
    cur_list.append([val, i])
    used_x += cnt

# x[0] 오름차순, x[1] 오름차순 정렬 (같은 값이면 낮은 id에 더해주는 조건)
cur_list.sort(key=lambda x: (x[0], x[1]))
for i in range(X - used_x):
    idx = cur_list[i][1]
    cur_list[i][0] += increase_list[idx]

cur_list.sort(key=lambda x: x[1])  # ID를 기준으로 정렬

print(*(item[0] for item in cur_list))
