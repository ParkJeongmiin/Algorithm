from collections import deque


def solution(board, commands):
    # ----- 1. 초기 설정 -----    
    N, M = len(board), len(board[0])
    dy = [0, 0, 1, 0, -1]     # 우, 하, 좌, 상
    dx = [0, 1, 0, -1, 0]
    
    # ----- 2. 함수 정의 -----
    # process
    def process(target_id, cond):
        group = find_group(target_id, cond)
        move_group(group, cond)
        
        while True:
            sliced_group = find_sliced_group(cond)
            if not sliced_group:
                break
            
            sliced_id = sliced_group.popleft()
            new_group = find_group(sliced_id, cond)
            move_group(new_group, cond)
        
        return False
    

    def find_group(target_id, cond):       
        group = set([target_id])
        queue = deque([target_id])      # 연속적으로 붙어있는 앱들을 찾기 위한 큐
        
        while queue:
            curr_id = queue.popleft()
            
            for y in range(N):
                for x in range(M):
                    if board[y][x] != curr_id: continue     # 현재 확인하는 앱과 다르면 넘어가기
                    
                    ny = (y + dy[cond] + N) % N
                    nx = (x + dx[cond] + M) % M
                    
                    next = board[ny][nx]
                    if next not in group and next != 0:     # 앱이 있는 자리이고 방문하지 않았던 곳이라면 큐와 그룹에 추가
                        queue.append(next)
                        group.add(next)
        return group
    
    
    def move_group(group, cond):
        cell_info = set([])
        
        # 이동해야 하는 좌표들 정보 추출
        for y in range(N):
            for x in range(M):
                if board[y][x] in group:
                    cell_info.add((y, x, board[y][x]))
                    
        # 기존에 있던 앱 정보 지우기
        for y, x, id in cell_info:
            board[y][x] = 0
            
        # 이동한 정보 입력
        for y, x, id in cell_info:
            ny = (y + dy[cond] + N) % N
            nx = (x + dx[cond] + M) % M
            board[ny][nx] = id
            
    
    # find_sliced_group
    def find_sliced_group(cond):
        sliced_id = deque([])
        visited = [0] * 101
        
        if cond == 1 or cond == 3:
            for y in range(N):
                # 행의 양끝이 같고, 새로 방문하는 id의 앱인 경우
                if (board[y][0] == board[y][-1]) and (board[y][0] != 0) and (visited[board[y][0]] == 0):
                    
                    # 전체 행을 가득 채우는 앱인지 확인
                    check = False
                    for x in range(M):
                        if board[y][x] != board[y][0]:
                            check = True
                            break
                    
                    if check:
                        visited[board[y][0]] = 1
                        sliced_id.append(board[y][0])
        else:
            for x in range(M):
                if (board[0][x] == board[-1][x]) and (board[0][x] != 0) and (visited[board[0][x]] == 0):
                    
                    check = False
                    for y in range(N):
                        if board[y][x] != board[0][x]:
                            check = True
                            break
                    
                    if check:
                        visited[board[0][x]] = 1
                        sliced_id.append(board[0][x])
        
        return sliced_id
                
    
    # ----- 3. 앱 정리 시뮬레이션 -----
    for target_id, cond in commands:
        process(target_id, cond)
    
    return board