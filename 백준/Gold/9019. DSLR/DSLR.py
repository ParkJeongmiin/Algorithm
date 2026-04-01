import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline
T = int(input())

# ----- code -----
# initial settings
outs = []
for _ in range(T):
    A, B = map(int, input().split())

    visited = [False] * 10000
    parent = [0] * 10000
    command = [""] * 10000

    queue = deque([A])
    visited[A] = True
    found = False

    while queue and not found:
        cur_value = queue.popleft()

        # D 연산
        new_value = (cur_value * 2) % 10000
        if not visited[new_value]:
            visited[new_value] = True
            parent[new_value] = cur_value
            command[new_value] = "D"
            if new_value == B:
                break
            queue.append(new_value)

        # S 연산
        new_value = (cur_value - 1) % 10000
        if not visited[new_value]:
            visited[new_value] = True
            parent[new_value] = cur_value
            command[new_value] = "S"
            if new_value == B:
                break
            queue.append(new_value)

        # L 연산
        new_value = (cur_value % 1000) * 10 + (cur_value // 1000)
        if not visited[new_value]:
            visited[new_value] = True
            parent[new_value] = cur_value
            command[new_value] = "L"
            if new_value == B:
                break
            queue.append(new_value)

        new_value = (cur_value % 10) * 1000 + (cur_value // 10)
        if not visited[new_value]:
            visited[new_value] = True
            parent[new_value] = cur_value
            command[new_value] = "R"
            if new_value == B:
                break
            queue.append(new_value)

    # 정답 출력
    idx = B
    answer = []
    while idx != A:
        answer.append(command[idx])
        idx = parent[idx]

    outs.append("".join(answer[::-1]))

sys.stdout.write("\n".join(outs) + "\n")
