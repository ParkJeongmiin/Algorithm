import sys
from collections import deque

"""
# 1단계 회전
1. belt(벨트 내구도 관리), robot(로봇 위치 관리) - deque
2. belt, robot 한 칸씩 회전
3. 회전 후, (N - 1) 위치에 로봇이 있으면 내리기

# 2단계 로봇 이동
1. robot 역순으로 이동 가능 여부 판단
    - 다음 칸 : 로봇 없고, 내구도가 1 이상
    - 이동한 다음 (N - 1) 위치면 내리기

# 3단계 로봇 올리기
1. belt[0]의 내구도가 0 아니면, 로봇 올리고, 내구도 1 감소

# 4단계 총 내구도 검사
1. 내구도가 0인 칸 계산 - K 이상이면 종료
"""

# ----- input -----
input = sys.stdin.readline
N, K = map(int, input().split())

# ----- code -----
# initial settings
belt = deque(list(map(int, input().split())))
robot = deque([False] * N)

step = 0

while True:
    step += 1

    # 1단계 회전
    belt.rotate(1)
    robot.rotate(1)

    robot[N - 1] = False

    # 2단계 로봇 이동
    for i in range(N - 2, -1, -1):  # (N - 2)부터 0까지 탐색
        if robot[i] and not robot[i + 1] and belt[i + 1] >= 1:
            robot[i] = False
            robot[i + 1] = True
            belt[i + 1] -= 1

            if i + 1 == N - 1:
                robot[i + 1] = False

    # 3단계 로봇 올리기
    if belt[0] > 0:
        robot[0] = True
        belt[0] -= 1

    # 4단계 총 내구도 검사
    if belt.count(0) >= K:
        break

print(step)
