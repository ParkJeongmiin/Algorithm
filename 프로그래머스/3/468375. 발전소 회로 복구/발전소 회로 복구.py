import heapq
from collections import deque


def solution(h, grid, panels, seqs):
    answer = 0
    n, m, k = len(grid), len(grid[0]), len(panels)
    
    # 엘리베이터(@) 위치 확인
    for y in range(n):
        for x in range(m):
            if grid[y][x] == '@':
                elevator = (y, x)
                break
    
    
    def bfs(sy, sx):
        '''시작 좌표를 입력 받아 해당 층에서 
        모든 구역까지 거리를 나타내는 2차원 배열을 반환하는 함수'''
        dy = [-1, 1, 0, 0]
        dx = [0, 0, -1, 1]
        
        visited = [[-1] * m for _ in range(n)]
        visited[sy][sx] = 0
        
        queue = deque([])
        queue.append((sy, sx))
        
        while queue:
            y, x = queue.popleft()
            
            for i in range(4):
                ny = y + dy[i]
                nx = x + dx[i]
                
                if (0 <= ny < n) and (0 <= nx < m):
                    if visited[ny][nx] == -1 and grid[ny][nx] != "#":
                        visited[ny][nx] = visited[y][x] + 1
                        queue.append((ny, nx))
        return visited


    # 패널-@, 패널-패널(같은 층 끼리만) 거리 계산 - BFS 예정
    # 기준 패널을 순회하면서 엘리베이터와 같은 층 패널 간 거리 정보를 2차원 배열에 저장
    dist_info = [[-1] * (k + 1) for _ in range(k)] # 패널-(패널, 엘리베이터) 간 거리 정보
    for si, (sf, sr, sc) in enumerate(panels):
        dist_map = bfs(sr - 1, sc - 1)
        
        # 엘리베이터 거리 저장
        dist_info[si][-1] = dist_map[elevator[0]][elevator[1]]        

        # 같은 층에 있는 패널과의 거리 저장
        for ei, (ef, er, ec) in enumerate(panels):
            if si == ei:
                dist_info[si][ei] = 0
                continue
                
            if dist_info[si][ei] != -1: # 자기 자신 or 이미 계산된 거리는 제외
                continue

            if sf == ef:
                dist_info[si][ei] = dist_map[er - 1][ec - 1]
                dist_info[ei][si] = dist_map[er - 1][ec - 1]

    # 제약 조건 정리 bit 연산을 통해 사전 조건 표현 : prereq_mask
    prereq_mask = [0] * k
    for pre_panel, post_panel in seqs:
        prereq_mask[post_panel - 1] |= (1 << (pre_panel - 1))   # post_panel의 기존 조건과 새로운 조건의 OR 연산으로 제약 조건 갱신

    # 다익스트라 큐
    INF = float('inf')
    dp = [[INF] * (1 << k) for _ in range(k)]
    
    queue = [(0, 0, 0)] # (time, 활성화 할 패널 idx 0-based, 현재 활성화 상태)
    dp[0][0] = 0    # 시작 위치와 상태에서는 0초로 시작
    
    while queue:
        curr_time, curr_panel, curr_state = heapq.heappop(queue)
        
        # [최적화] : 현재 상태 결과가 기존보다 큰 값이면 제외
        if dp[curr_panel][curr_state] < curr_time:
            continue
            
        # [종료] : 모든 패널이 활성화 되었다면, 다익스트라 특성 상 가장 먼저 완료된 결과가 '최소 조건'
        if curr_state == (1 << k) - 1:
            return curr_time
        
        # 다음 활성화 패널 탐색
        for next_panel in range(k):
            if curr_state & (1 << next_panel):   # 이미 활성화된 패널은 제외
                continue
                
            if (curr_state & prereq_mask[next_panel]) != prereq_mask[next_panel]: # 목표 패널의 제약 조건을 만족하지 않으면 제외
                continue
            
            # 현재, 다음 패널 간의 거리 계산(같은 층, 다른 층 분기 처리)
            if panels[curr_panel][0] == panels[next_panel][0]:
                tmp_time = dist_info[curr_panel][next_panel]
            else:
                tmp_time = dist_info[curr_panel][-1] + dist_info[next_panel][-1] + abs(panels[curr_panel][0] - panels[next_panel][0])
            
            # 목표를 기준으로 다음 시간과 활성화 마스크 계산
            next_time = curr_time + tmp_time
            next_state = curr_state | (1 << next_panel)
            
            # next_time이 기존 기록된 기록보다 작으면 dp_table 갱신 + heapq에 추가
            if next_time < dp[next_panel][next_state]:
                dp[next_panel][next_state] = next_time
                heapq.heappush(queue, (next_time, next_panel, next_state))
    
    # 모든 조건을 만족하지 못한다면 -1 return
    return -1