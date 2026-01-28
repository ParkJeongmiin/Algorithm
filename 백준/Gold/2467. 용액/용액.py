import sys

# ----- input -----
input = sys.stdin.readline
N = int(input())
samples = list(map(int, input().split()))

# ----- code -----
# initial settings
INF = sys.maxsize
low_idx, high_idx = 0, N - 1
cur_min_sum_val = INF
answer = [0, 0]

while low_idx < high_idx:
    sum_value = samples[low_idx] + samples[high_idx]

    if sum_value == 0:
        answer[0], answer[1] = samples[low_idx], samples[high_idx]
        break

    if abs(sum_value) < cur_min_sum_val:
        cur_min_sum_val = abs(sum_value)
        answer[0], answer[1] = samples[low_idx], samples[high_idx]

    if sum_value < 0:
        low_idx += 1
    else:
        high_idx -= 1

print(answer[0], answer[1])