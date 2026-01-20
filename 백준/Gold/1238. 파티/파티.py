import sys
import heapq

"""
N 명 학생, M개 노드, X에서 파티
# 그래프 탐색, 최단 경로 -> 다익스트라 알고리즘

1. 리스트에 그래프 정보 저장
    graph[i] : i 번째 노드에서 (j, t) j번째 까지 t 소요

2. X를 제외한 노드들로 왕복 거리 계산 (N - 1번 연산)
    1) 돌아오는 길 (X -> N_i)
        X에서 모든 노드로 가는 최단 거리를 한 번 계산하면 된다.

    2) 가는 길 (N_i -> X)
        N_i를 순회하면서 X까지 최단 거리를 계산할 수 있지만, 
        (N - 1) 번의 연산이 필요하고 N이 커지면 시간이 오래 걸린다.

        그래서, 그래프의 간선을 모두 역방향으로 변환해
        X에서 모든 노드까지 최단 거리를 계산하면 계산량을 줄일 수 있다.
"""

# ----- input -----
input = sys.stdin.readline
INF = sys.maxsize
N, M, X = map(int, input().split())

# ----- code -----
# initial settings
# graph, reverse_graph 생성
graph = [[] for _ in range(N + 1)]
reverse_graph = [[] for _ in range(N + 1)]

for _ in range(M):
    u, v, t = map(int, input().split())
    graph[u].append((v, t))
    reverse_graph[v].append((u, t))


# 다익스트라 알고리즘
def dijkstra(start_node, graph):
    distance = [INF] * (N + 1)  # 거리 정보 리스트
    distance[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))  # (비용, 노드)

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        if distance[cur_node] < cur_distance:  # 이미 계산된 거리보다 크면 스킵
            continue

        for next_node, weight in graph[cur_node]:  # 현재 노드와 연결된 노드 탐색
            new_distance = cur_distance + weight

            # 새로 계산된 경로가 더 작으면 업데이트
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))

    return distance


from_party = dijkstra(X, graph)  # graph로 X에서 다익스트라 알고리즘
to_party = dijkstra(X, reverse_graph)  # reverse_graph로 X에서 다익스트라 알고리즘


answer = 0
for i in range(1, N + 1):
    if from_party[i] != INF and to_party[i] != INF:
        answer = max(answer, from_party[i] + to_party[i])

print(answer)
