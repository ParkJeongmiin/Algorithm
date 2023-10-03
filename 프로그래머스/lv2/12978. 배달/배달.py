import heapq
from math import inf

def solution(N, road, K):
    answer = 0

    # 거리 기록 테이블
    dist = [inf] * (N+1)
    dist[1] = 0
    
    # 그래프 생성    [[node_a, node_b, cost]]
    graph = [[] for _ in range(N+1)]
    for a, b, c in road:
        graph[a].append([c, b])
        graph[b].append([c, a])
    
    # 다익스트라 알고리즘
    heap = []
    heapq.heappush(heap, [0, 1])    # [cost, node]
    
    while heap:
        cost, node = heapq.heappop(heap)    # 현재 거리, 노드 pop
        
        for c, n in graph[node]:        # 다음 노드에 대한 정보 가져오기
            if cost + c < dist[n]:      # 새로 구한 시간 < 기존 시간 : 갱신
                dist[n] = cost + c
                heapq.heappush(heap, [cost+c, n])
    
    # 결과 출력
    for dist in dist:
        if dist <= K:
            answer += 1
    
    return answer