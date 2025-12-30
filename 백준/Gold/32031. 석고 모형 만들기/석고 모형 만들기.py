"""
원기둥 축과 연결 -> 경우의 수 너무 많음
=> 완전 탐색 불가

하나의 정육면체를 8개의 작은 조각으로 변형
(r, c, y, x, z)
r, c    -> 큰 정육면체 구분
y       -> 세로(행) 방향 구분(위 / 아래)
x       -> 가로(열) 방향 구분(좌 / 우)
z       -> 높이 방향 구분(바닥 / 천장)

# 원기둥 축 방향에 따른 간선 변화
## "O" => z를 통해 연결
    (r, c, y, x, 0) - (r, c, y, x, 1)

## "I" => x를 통해 연결
    (r, c, y, 0, z) - (r, c, y, 1, z)

## "H" => y를 통해 연결
    (r, c, 0, x, z) - (r, c, 1, x, z)

# 큰 정육면치 끼리 만나는 경우 간선 변화
## 오른쪽 칸과 연결 => 왼쪽의 오른쪽 조각(x = 1)과 오른쪽의 왼쪽 조각(x = 0) 연결
    (r, c, y, 1, z) - (r, c+1, y, 0, z)

## 아래 칸과 연결 => 위쪽의 아래칸 조각(y = 1)과 아래쪽의 위쪽 조각(y = 0) 연결
    (r, c, 1, x, z) - (r+1, c, 0, x, z)

1. 큰 정육면체를 순회
2. command 명령에 따라 내부 간선들 연결
3. 외부 블럭과 연결된 경우 외부 간선 간 연결
4. 독립된 그룹의 갯수 계산(using Union-find)
"""

import sys

# ----- input -----
input = sys.stdin.readline
R, C = map(int, input().split())
grid = [input().strip() for _ in range(R)]


# ----- code -----
def find(x):
    """노드 id(x)의 부모 노드 id를 찾는 함수"""
    if parents[x] == x:
        return x
    parents[x] = find(parents[x])
    return parents[x]


def union(x, y):
    """두 노드의 부모 노드가 다른 경우 하나의 그룹으로 병합"""
    root_X = find(x)
    root_Y = find(y)

    if root_X != root_Y:
        parents[root_Y] = root_X
        return True

    return False


def get_id(r, c, dy, dx, dz):
    """3차원 노드를 1차원의 고유 ID를 부여하는 함수"""
    return (r * C + c) * 8 + (4 * dy + 2 * dx + dz)


total_nodes = R * C * 8
parents = list(range(total_nodes))  # 각 노드 id 별 부모 노드의 id를 표시

for r in range(R):
    for c in range(C):
        command = grid[r][c]

        # 1. 원기둥 방향 별, 내부 노드 연결
        if command == "O":  # (r, c, 0, x, z) - (r, c, 1, x, z)
            for dy in range(2):
                for dx in range(2):
                    u = get_id(r, c, dy, dx, 0)
                    v = get_id(r, c, dy, dx, 1)
                    union(u, v)
        elif command == "H":  # (r, c, y, 0, z) - (r, c, y, 1, z)
            for dy in range(2):
                for dz in range(2):
                    u = get_id(r, c, dy, 0, dz)
                    v = get_id(r, c, dy, 1, dz)
                    union(u, v)
        elif command == "I":  # (r, c, 0, x, z) - (r, c, 1, x, z)
            for dx in range(2):
                for dz in range(2):
                    u = get_id(r, c, 0, dx, dz)
                    v = get_id(r, c, 1, dx, dz)
                    union(u, v)

        # 2. 외부 정육면체 연결로 인한 노드 병합
        # 오른쪽 블럭과 연결
        if c + 1 < C:  # (r, c, y, 1, z) - (r, c+1, y, 0, z)
            for dy in range(2):
                for dz in range(2):
                    u = get_id(r, c, dy, 1, dz)
                    v = get_id(r, c + 1, dy, 0, dz)
                    union(u, v)

        # 아래쪽 블럭과 연결
        if r + 1 < R:  # (r, c, 1, x, z) - (r+1, c, 0, x, z)
            for dx in range(2):
                for dz in range(2):
                    u = get_id(r, c, 1, dx, dz)
                    v = get_id(r + 1, c, 0, dx, dz)
                    union(u, v)

# 독립된 그룹의 갯수 계산
# 모든 노드에 대해 부모 노드 최신화 진행후 Set에 저장
unique_roots = set()
for i in range(total_nodes):
    unique_roots.add(find(i))

print(len(unique_roots))
