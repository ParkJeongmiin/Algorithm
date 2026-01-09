import sys
from collections import deque

# ----- input -----
input = sys.stdin.readline

N, Q = map(int, input().split())

# ----- code -----
# 그래프 구성 - 인접리스트(양방향 연결)
graph = [[] for _ in range(N + 1)]

for _ in range(N - 1):
    p, q, r = map(int, input().split())

    graph[p].append((q, r))
    graph[q].append((p, r))

# 질문 Q(k, v)별로
for _ in range(Q):
    k, v = map(int, input().split())

    visited = [False] * (N + 1)
    visited[v] = True
    queue = deque([v])
    answer = 0

    while queue:
        cur_node = queue.pop()

        for next_node, weight in graph[cur_node]:
            # 방문하지 않은 노드이고, USADO 조건(가중치 >= k) 만족하면 queue에 넣기
            if not visited[next_node] and weight >= k:
                queue.append(next_node)
                visited[next_node] = True
                answer += 1

    print(answer, end="\n")
