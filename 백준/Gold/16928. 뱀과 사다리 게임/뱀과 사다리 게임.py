import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline
N, M = map(int, input().split())

# ----- code -----
info = {}
for _ in range(N + M):
    x, y = map(int, input().split())
    info[x] = y

dist = [-1] * 101
dist[1] = 0  # 시작 위치 횟수 설정
queue = deque([1])  # 시작 위치 설정

while queue:
    cur_num = queue.popleft()

    if cur_num == 100:
        print(dist[cur_num])
        break

    for i in range(1, 7):
        next_num = cur_num + i

        if next_num <= 100:
            if next_num in info:
                next_num = info[next_num]

            if dist[next_num] == -1:
                queue.append(next_num)
                dist[next_num] = dist[cur_num] + 1
