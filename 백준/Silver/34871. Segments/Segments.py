import sys

input = sys.stdin.readline
N, Q = map(int, input().split())

max_l, min_r = 0, sys.maxsize
for _ in range(N):
    l, r, _ = map(int, input().split())
    max_l = max(max_l, l)
    min_r = min(min_r, r)

# ----- code -----
for _ in range(Q):
    query = int(input())
    print(max(0, max_l - query, query - min_r), end="\n")