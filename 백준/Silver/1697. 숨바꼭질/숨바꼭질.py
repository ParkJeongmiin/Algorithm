from collections import deque

n, k = map(int, input().split())
map = [-1] * 100001

def bfs(n):
    queue = deque()
    queue.append(n)
    
    while queue:
        node = queue.popleft()
        
        for i in (node + 1, node - 1, node * 2):
            if i < 0 or i > 100000 : continue
            if map[i] == -1:
                queue.append(i)
                map[i] = map[node] + 1
    
map[n] = 0
bfs(n)
print(map[k])