import sys

# ----- input -----
input = sys.stdin.readline
N, r, c = map(int, input().split())

# ----- code -----
counts = 0

while N > 0:
    N -= 1
    half = 2**N
    flag = -1

    if r < half and c < half:  # 1 사분면
        pass
    elif r < half and c >= half:  # 2 사분면
        flag = 2
        counts += half * half
        c -= half
    elif r >= half and c < half:  # 3 사분면
        flag = 3
        counts += 2 * half * half
        r -= half
    else:  # 4 사분면
        flag = 4
        counts += 3 * half * half
        r -= half
        c -= half

print(counts)
