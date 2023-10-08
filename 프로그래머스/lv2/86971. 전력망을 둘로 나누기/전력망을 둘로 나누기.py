from collections import deque

def solution(n, wires):
    answer = 101
    
    graph = [[] for _ in range(n+1)]

    for v1, v2 in wires:                # 그래프 생성
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    def bfs(start):
        visited = [0] * (n+1)
        queue = deque()
        queue.append(start)
        visited[start] = 1
        count = 1
        
        while queue:
            cur_node = queue.popleft()
            
            for next_node in graph[cur_node]:
                if not visited[next_node]:
                    visited[next_node] = 1
                    queue.append(next_node)
                    count += 1
        return count

    # 간선 하나씩 자르고 개수 비교
    for v1, v2 in wires:
        graph[v1].remove(v2)
        graph[v2].remove(v1)
        
        answer = min(answer, abs(bfs(v1) - bfs(v2)))
        
        graph[v1].append(v2)
        graph[v2].append(v1)
        
    return answer
'''
wires에서 하나르 없애서 그 때, 두 전력망의 노드 개수 차이를 구한다. 
현재 차이값이 기존 값보다 작으면 answer 갱신
'''