def solution(park, routes):
    size_x, size_y = -1, -1
    x, y = 0, 0
    
    # 시작 위치, 공원 크기 구하기
    for height in range(len(park)):
        for width in range(len(park[height])):
            if park[height][width] == 'S':
                x, y = height, width     
                
    size_x, size_y = height, width

    # 이동 방향 정의
    op = {'N' : (-1, 0), 'S' : (1, 0), 'W' : (0, -1), 'E' : (0, 1)}
    
    # 명령에 따라 위치 이동
    for i in routes:
        # 명령에 맞는 dx, dy 가져오기
        dx, dy = op[i.split()[0]]
        n = int(i.split()[1])
        
        moved_x, moved_y = x, y     # 이동 하는 동안의 좌표
        state = True                # 이동 가능한지 판단
        
        # 이동
        for _ in range(n):
            nx = moved_x + dx
            ny = moved_y + dy
            
            # 공원 안 and 장애물 없다 => 이동 가능
            if 0 <= nx <= size_x and 0 <= ny <= size_y and park[nx][ny] != 'X':
                state = True
                moved_x = nx
                moved_y = ny
            else:
                state = False
                break
        
        # 현재 위치로 업데이트
        if state:
            x, y = nx, ny
        
    return [x, y]