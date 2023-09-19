n = int(input())    # 컴퓨터 개수
v = int(input())    # 간선 수

visited = [0] * (n+1)
graph = [[] for _ in range(n+1)]

for v in range(v):
    a, b = map(int, input().split())
    graph[a] += [b]
    graph[b] += [a]    # 양방향 연결
    
def dfs(node):
    visited[node] = 1    # 현재 노드 방문 처리
    
    for next in graph[node]:
        if visited[next] == 0:
            dfs(next)
            
dfs(1)
print(sum(visited) - 1)