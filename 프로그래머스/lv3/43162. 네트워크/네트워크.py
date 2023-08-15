def dfs(n, computers, start, visited):
    visited[start] = True
    
    for node in range(n):
        if visited[node] == False and computers[start][node] == 1:
        # 현재 노드가 방문하지 않은 노드이고 + 다른 노드와 연결되어 있다면 -> DFS 탐색해서 끝까지 진행
            visited = dfs(n, computers, node, visited)
    return visited
            

def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for start in range(n):
        if visited[start] == False:
            dfs(n, computers, start, visited)
            answer += 1
    
    return answer
