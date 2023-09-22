from collections import deque

def solution(begin, target, words):
    
    if target not in words:
        return 0
    
    visited = [False for _ in range(len(words))]    # 방문 현황
    queue = deque()
    queue.append([begin, 0])                        # [현재 단어, 깊이]
    
    while queue:
        node, count = queue.popleft()               # 현재 노드 추출
        
        if node == target:                          # 현재 노드가 target이면 깊이 출력
            return count
        
        for i in range(len(words)):                 # 단어를 하나씩 가져와서
            diff = 0
            
            if not visited[i]:                      # 방문하지 않았던 단어이면
                for j in range(len(node)):          # 한 글자씩 비교한다.
                    if node[j] != words[i][j]:      # 알파벳이 다르면 diff 1 증가
                        diff += 1
                    
                if diff == 1:                       # 단어가 한 글자만 다르면
                    queue.append([words[i], count + 1])     # 그 단어를 다음 방문할 노드 큐에 삽입하고
                    visited[i] = True               # 방문 처리한다.