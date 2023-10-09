from collections import deque

def solution(n, edge):
    answer = 0
    
    visited = [-1] * (n + 1)
    graph = [[] for _ in range(n + 1)]
    for v1, v2 in edge:
        graph[v1].append(v2)
        graph[v2].append(v1)
    
    queue = deque([])
    queue.append(1)
    visited[1] = 0
    
    while queue:
        cur_node = queue.popleft()
        
        for next_node in graph[cur_node]:
            if visited[next_node] == -1:
                visited[next_node] = visited[cur_node] + 1
                queue.append(next_node)

    return visited.count(max(visited))
'''
n개 노드
가장 멀리 떨어진 노드의 갯수

>> bfs
visited에 1부터 해당 노드까지 거리의 거리를 저장한다.
'''