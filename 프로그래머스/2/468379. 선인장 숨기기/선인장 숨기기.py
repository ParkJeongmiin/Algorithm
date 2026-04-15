import sys
from collections import deque


def solution(m, n, h, w, drops):
    # ----- 1. 전체 maps 설정 -----
    # 비가 오지 않는 구역은 INF, 비가 오는 구역은 해당 idx 값 부여
    INF = sys.maxsize
    maps = [[INF] * n for _ in range(m)]
    
    for i, (r, c) in enumerate(drops):
        maps[r][c] = i
        
    # ----- 2. 행 단위 가로 윈도우 최솟값 계산 -----
    row_min_maps = [[0] * (n - w + 1) for _ in range(m)]
    
    for r in range(m):
        row_mins = deque()  # 행 마다 큐 초기화
        
        for c in range(n):
            v = maps[r][c]
            
            # 다음 들어오는 값이 rear 보다 작거나 같으면, rear는 절대 최솟값이 될 수 없으므로 pop
            while row_mins and row_mins[-1][1] >= v:
                row_mins.pop()
                
            row_mins.append((c, v))     # 다음 들어올 값 큐에 추가
            
            # 가로 윈도우 범위를 벗어나는 앞쪽 값 제거
            if row_mins[0][0] <= c - w:
                row_mins.popleft()
            
            # 윈도우 크기를 만족한 뒤부터 최솟값 저장
            if c >= w - 1:
                row_min_maps[r][c - w + 1] = row_mins[0][1]
                
    # ----- 3. 열 단위 윈도우 최솟값 계산 및 최종 정답 갱신 -----
    best_val = -1               # 최댓값을 우선
    best_r, best_c = INF, INF   # 최솟값을 우선
    
    for c in range(n - w + 1):
        col_mins = deque()  # 열 마다 큐 초기화
        
        for r in range(m):
            v = row_min_maps[r][c]
            
            while col_mins and col_mins[-1][1] >= v:
                col_mins.pop()
                
            col_mins.append((r, v))
            
            if col_mins[0][0] <= r - h:
                col_mins.popleft()
            
            # 윈도우 세로 크기 만족한 뒤부터 최종 후보 비교, 갱신
            if r >= h - 1:
                curr_min_v = col_mins[0][1]
                curr_r, curr_c = r - h + 1, c
                
                # 우선순위 : 1. v 클수록, 2. r 작을수록, 3. c 작을수록
                if (curr_min_v, -curr_r, -curr_c) > (best_val, -best_r, -best_c):
                    best_val = curr_min_v
                    best_r = curr_r
                    best_c = curr_c
    
    return [best_r, best_c]