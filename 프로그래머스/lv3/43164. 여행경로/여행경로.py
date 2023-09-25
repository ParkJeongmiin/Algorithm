from collections import defaultdict

def solution(tickets):
    answer = []
    
    ''' 그래프 생성 '''
    graph = defaultdict(list)
    for src, dist in tickets:
        graph[src].append(dist)
        
    for key in graph:
        graph[key].sort(reverse = True)
    
    ''' 스택을 이용해 dfs 시작 '''
    stack = ['ICN']
    while stack:
        top = stack[-1]
        
        if top not in graph or not graph[top]:  # top에서 출발하는 티켓이 없는 경우
            answer.append(stack.pop())
        else:
            stack.append(graph[top].pop())
            
    return answer[::-1]