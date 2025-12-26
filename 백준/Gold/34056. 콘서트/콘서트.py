import sys

# ----- input -----
input = sys.stdin.readline

N = int(input())
D = list(map(int, input().split()))
Q = int(input())

# ----- code -----

# idx-1, idx 사이에 x 콘서트 발생
# 오른쪽만 가정한다면
# 1. D_c >= x   -> D_c += x (보강)
# 2. D_c < x    -> D_c += min(D_c, x) (보강), x - D_c 만큼 감당

for _ in range(Q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        # 왼쪽 확산 (idx -> 0)
        idx, x = query[1] - 1, query[2]
        while idx >= 0 and x > 0:
            if D[idx] < x:
                # 흡수력이 충분하지 못하는 경우 : 흡수된 소음을 왼쪽 벽으로 전달
                x -= D[idx]
                D[idx] *= 2
                idx -= 1
            else:
                # 벽이 모든 소음을 흡수할 수 있는 경우
                D[idx] += x
                x = 0
                break

        # 오른쪽 확산 (idx -> N)
        idx, x = query[1], query[2]
        while idx < N and x > 0:
            if D[idx] < x:
                # 흡수력이 충분하지 못하는 경우 : 흡수된 소음을 왼쪽 벽으로 전달
                x -= D[idx]
                D[idx] *= 2
                idx += 1
            else:
                # 벽이 모든 소음을 흡수할 수 있는 경우
                D[idx] += x
                x = 0
                break
    else:
        print(D[query[1] - 1], end="\n")
