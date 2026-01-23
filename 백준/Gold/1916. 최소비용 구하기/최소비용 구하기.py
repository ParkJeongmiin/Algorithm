import sys
import heapq

# ----- input -----
input = sys.stdin.readline

MAX = sys.maxsize
N = int(input())
M = int(input())


# ----- code -----
# dijkstra
def dijkstra(start_node, graph):
    distance = [MAX] * (N + 1)
    distance[start_node] = 0

    queue = []
    heapq.heappush(queue, (0, start_node))

    while queue:
        cur_distance, cur_node = heapq.heappop(queue)

        # 이미 계산된 거리가 작으면 스킵
        if distance[cur_node] < cur_distance:
            continue

        # 현재 노드와 연결된 모든 노드 순회
        for next_node, weight in graph[cur_node]:
            new_distance = cur_distance + weight

            # 현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if new_distance < distance[next_node]:
                distance[next_node] = new_distance
                heapq.heappush(queue, (new_distance, next_node))

    return distance


# initial settings
graph = [[] for _ in range(N + 1)]

for _ in range(M):
    start, end, weight = map(int, input().split())
    graph[start].append((end, weight))

# 최저 비용 계산
start, end = map(int, input().split())
outputs = dijkstra(start, graph)

print(outputs[end])
