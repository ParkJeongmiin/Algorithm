from collections import defaultdict


def solution(n, infection, edges, k):
    # 타입 별 배양체 번호 저장
    graph = defaultdict(lambda: defaultdict(list))
    for u, v, t in edges:
        graph[t][u - 1].append(v - 1)
        graph[t][v - 1].append(u - 1)
    
    # 타입 별 연결된 배양체 구성요소 그룹 계산 - BFS, bit
    type_components = defaultdict(list)
    for t in [1, 2, 3]:
        visited = set()
        
        for i in range(n):
            if i not in visited:
                # 방문 처리와 탐색할 그룹 시작 위치 지정
                q = [i]
                visited.add(i)
                
                # 연결 그룹 저장을 위한 bit mask 초기 설정
                comp_mask = 0
                comp_size = 0
                
                # 그룹 탐색을 위한 BFS
                while q:
                    curr_node = q.pop()
                    comp_mask |= (1 << curr_node)   # 같은 그룹 위치에 masking using OR calc
                    comp_size += 1
                    
                    for neighbor_node in graph[t][curr_node]:   # 같은 파이프로 연결된 노드 정보
                        if neighbor_node not in visited:
                            q.append(neighbor_node)
                            visited.add(neighbor_node)
                
                if comp_size >= 2:  # 단일 노드를 제외한 그룹만 저장
                    type_components[t].append(comp_mask)
    
    # 최대 감염 배양체 계산
    initial_state = (1 << infection - 1)    # 초기 감염 상태 초기화(bit, 0-based index)
    checked_infections = {initial_state}    # 단계별 감염 시나리오 관리(Set, bit-integer)
    max_infection = 1   # 최대 감염 배양체 초기화
    
    queue = [initial_state] # 현재 세대에서 탐색해야 하는 배양체 정보
    for _ in range(k):      # 전체 배양체 순회
        next_queue = []     # 다음 세대 관리 큐 초기화(이전 단계에서 감염된 배양체 번호)
        
        for state in queue:
            for t in [1, 2, 3]:
                curr_state = state
                
                # 그룹을 순회하면서 하나라도 겹치는 배양체가 있다면 같은 그룹 전체 감염
                for comp_mask in type_components[t]:
                    if curr_state & comp_mask:
                        curr_state |= comp_mask
                        
                # 해당 단계의 감염 시나리오가 이전에 발견된 적이 있는지 확인
                # 이전에도 같은 시나리오가 있으면 이후에는 같기 때문에 가지치기
                # 새로운 시나리오라면 "현재 시나리오 추가", "다음 세대 확인할 큐 추가", "최대 배양체 개수 갱신"
                if curr_state not in checked_infections:
                    checked_infections.add(curr_state)
                    next_queue.append(curr_state)
                    max_infection = max(max_infection, bin(curr_state).count("1"))        
    
        queue = next_queue  # 현재 세대 큐 = 다음 세대 큐
    
    return max_infection