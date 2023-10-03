import sys
import heapq

input = sys.stdin.readline
V, E = map(int, input().split())
start = int(input())

INF = sys.maxsize
distance = [INF] * (V + 1)
distance[start] = 0

graph = [[] for _ in range(V + 1)]
for _ in range(E):
    u, v, w = map(int, input().split())
    graph[u].append((w, v))    # [node, cost]
    
# 다익스트라 알고리즘
heap = []
heapq.heappush(heap, (0, start))    # [cost, node]

while heap:
    cost, node = heapq.heappop(heap)
    
    for c, n in graph[node]:
        if cost + c < distance[n]:
            distance[n] = cost + c
            heapq.heappush(heap, [cost + c, n])
            
for i in range(1, len(distance)):
    if distance[i] != INF:
        print(distance[i])
    else:
        print('INF')