import sys

# ----- input -----
input = sys.stdin.readline
N, M = map(int, input().split())

# ----- code -----
# initial settings
visited = [[False] * M for _ in range(N)]
maps = []
for _ in range(N):
    layer = list(map(int, input().split()))
    maps.append(layer)

dy = [-1, 1, 0, 0]
dx = [0, 0, -1, 1]

answer = 0
max_value = max(map(max, maps))


# dfs
def dfs(y, x, depth, val):
    global answer

    if depth == 4:  # 기저 조건
        answer = max(answer, val)
        return

    if answer >= val + max_value * (4 - depth):  # 호출 스택 효율을 위한 가지 치기
        return

    for i in range(4):  # 상하좌우 순회
        ny = y + dy[i]
        nx = x + dx[i]

        if 0 <= ny < N and 0 <= nx < M and not visited[ny][nx]:
            visited[ny][nx] = True  # y, x 방문 처리
            dfs(ny, nx, depth + 1, val + maps[ny][nx])
            visited[ny][nx] = False  # y, x 방문 처리 해제


for y in range(N):
    for x in range(M):
        visited[y][x] = True
        dfs(y, x, 1, maps[y][x])
        visited[y][x] = False

        # 'ㅗ' 모양 예외 처리
        center = maps[y][x]

        target_list = []
        for i in range(4):
            ny = y + dy[i]
            nx = x + dx[i]

            if 0 <= ny < N and 0 <= nx < M:
                target_list.append(maps[ny][nx])

        if len(target_list) == 4:
            answer = max(answer, center + sum(target_list) - min(target_list))
        elif len(target_list) == 3:
            answer = max(answer, center + sum(target_list))

print(answer)
