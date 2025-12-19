import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline

N = int(input())

K = int(input())
apples = []
for _ in range(K):
    y, x = map(int, input().split())
    apples.append([y - 1, x - 1])

C = int(input())
dir_info = deque()
for _ in range(C):
    t, d = input().split()
    t = int(t)
    dir_info.append([t, d])

# ----- code -----
# 상, 우, 하, 좌
dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dir_idx = 1


def change_dir(d):
    global dir_idx
    if d == "D":  # 시계 방향 회전
        if dir_idx == 3:
            dir_idx = 0
        else:
            dir_idx += 1
    else:  # 반시계 방향 회전
        if dir_idx == 0:
            dir_idx = 3
        else:
            dir_idx -= 1


maps = [[0 for _ in range(N)] for _ in range(N)]
for y, x in apples:
    maps[y][x] = 1
y, x, t = 0, 0, 0

body = deque()
body.append([0, 0])

while True:
    t += 1  # 시간 경과
    y += dy[dir_idx]  # 방향 이동
    x += dx[dir_idx]  # 방향 이동

    if (0 <= y < N) and (0 <= x < N) and ([y, x] not in body):
        if maps[y][x] == 1:  # 사과인 경우
            maps[y][x] = 0
            body.append([y, x])
        else:  # 사과가 없는 경우
            body.append([y, x])
            body.popleft()
    else:
        break

    if dir_info and (dir_info[0][0] == t):
        change_dir(dir_info[0][1])
        dir_info.popleft()

print(t)
