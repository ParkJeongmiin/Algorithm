def solution(grid):
    answer = 0
    
    # initial settings
    n = len(grid)
    m = len(grid[0])
    
    dy = [-1, 1, 0, 0]  # 상하좌우
    dx = [0, 0, -1, 1]
    reverse_dir = [1, 0, 3, 2]
    mapping_table = [[2, 0, 7, 6], 
                    [0, 2, 4, 5], 
                    [5, 6, 1, 0], 
                    [4, 7, 0, 1]]
    
    initial_grid = [[grid[i][j] for j in range(m)] for i in range(n)]    # 원본 맵 백업
    visited = [[0] * m for _ in range(n)]     # tmp (0-based idx)
    visited[0][0] = 1
    
    # dfs 알고리즘
    def dfs(y, x, curr_dir): 
        nonlocal answer
        
        # 종료 조건 : 도착 지점에 도착했을 때
        if (y == n - 1) and (x == m - 1):
            is_valid = True
            
            for i in range(n):
                for j in range(m):
                    # 기존 설치된 선로를 모두 통과했는지 검증
                    if initial_grid[i][j] > 0 and visited[i][j] == 0:
                        is_valid = False
                        break
                    
                    # 3번 선로를 2번 통과했는지 검증
                    if grid[i][j] == 3 and visited[i][j] != 2:
                        is_valid = False
                        break
                
                if not is_valid:
                    break
            
            if is_valid:
                answer += 1
            
            return
        
        # 다음 탐색해야 할 cell 좌표 계산 - (y, x)의 레일과 방향에 의해 결정
        ny = y + dy[curr_dir]
        nx = x + dx[curr_dir]
        
        # (ny, nx)에 들어갈 수 있는 방향
        for next_dir in range(4):
            # 역방향 탐색 제외
            if reverse_dir[next_dir] == curr_dir:
                continue
            
            # 원하는 방향 별로 (ny, nx)에 놓을 선로 선택
            required_rail = mapping_table[curr_dir][next_dir]
            is_straight = (curr_dir == next_dir)
            
            # 범위를 벗어나거나 장애물을 만나면 탐색 제외
            if ny < 0 or ny >= n or nx < 0 or nx >= m or grid[ny][nx] == -1:
                continue
                
            # 탐색할 칸이 비어있는 경우
            if grid[ny][nx] == 0:
                if required_rail == 0:
                    continue
                
                # 가능한 선로 후보 탐색
                candidates = []
                candidates.append(required_rail)
                
                if is_straight:
                    candidates.append(3)
                
                # 가능한 후보들로 dfs 수행
                for rail in candidates:
                    grid[ny][nx] = rail
                    visited[ny][nx] += 1
                    
                    dfs(ny, nx, next_dir)
                    
                    grid[ny][nx] = 0
                    visited[ny][nx] -= 1
            else:
                existing_rail = grid[ny][nx]
                
                # 설치된 선로가 3번인 경우
                if existing_rail == 3:
                    if not is_straight or visited[ny][nx] >= 2:
                        continue
                # 선택한 선로와 기존 선로가 일치하지 않는 경우는 탐색 제외
                elif existing_rail != required_rail:
                    continue
                
                # 기존 선로가 3번이 아닌데 이미 방문한 구역이면 탐색 제외
                if existing_rail != 3 and visited[ny][nx] >= 1:
                    continue
                    
                # 가능한 레일 놓은 후 백트래킹
                visited[ny][nx] += 1
                dfs(ny, nx, next_dir)
                visited[ny][nx] -= 1
                
        return 0
    
    
    # 선로 결정 시뮬레이션
    dfs(0, 0, 3)
    
    return answer
