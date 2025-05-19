def get_path(start_r, start_c, end_r, end_c, output_list):
    """
    start부터 end까지 최단 경로의 모든 좌표를 계산하는 함수
    r 방향 이동을 c 보다 우선
    """
    cur_r, cur_c = start_r, start_c

    while not (cur_r == end_r and cur_c == end_c):
        if cur_r < end_r:
            cur_r += 1
        elif cur_r > end_r:
            cur_r -= 1
        elif cur_c < end_c:
            cur_c += 1
        else:
            cur_c -= 1
        
        output_list.append([cur_r, cur_c])


def solution(points, routes):
    answer = 0
    
    # points 별 최단 경로 좌표들 계산
    # point 별 좌표 초기화
    point_info = {}
    for i in range(len(points)):
        r, c = points[i]
        point_info[i + 1] = (r, c)
    
    # 로봇 별 모든 이동 경로 좌표 계산
    robot_paths = []
    
    for route in routes:
        # 초기 위치 설정
        start_point = route[0]
        start_r, start_c = point_info[start_point]
        output_list = [[start_r, start_c]]
        
        # 다음 도착 위치까지 이동 경로 좌표 계산
        for i in range(1, len(route)):
            end_point = route[i]
            
            # 출발, 도착 지점 정보 update
            start_r, start_c = point_info[start_point]
            end_r, end_c = point_info[end_point]
            
            # 출발 -> 도착까지 모든 좌표 정보 계산
            get_path(start_r, start_c, end_r, end_c, output_list)
            
            # 도착 지점을 다음 출발 지점으로 초기화
            start_point = end_point
            
        robot_paths.append(output_list)
    
    # 시간 대별 겹치는 좌표 계산
    time_max = max([len(robot_path) for robot_path in robot_paths])
    
    # 시간(i)마다 로봇 별(j) 좌표 확인
    for i in range(time_max):
        coord_set = set()
        danger_coord_set = set()
        
        for j in range(len(robot_paths)):
            # 종료된 경로인 경우 무시
            if len(robot_paths[j]) < (i + 1):
                continue
            
            # 같은 시간 대 로봇 위치
            r, c = robot_paths[j][i]
            
            # 위험 상황으로 처리된 좌표는 무시
            if (r, c) in danger_coord_set:
                continue
                
            # 최초로 위험 상황을 발견한 경우
            if (r, c) in coord_set:
                danger_coord_set.add((r, c))
                continue
            
            # 해당 좌표에 처음으로 로봇이 도착한 경우
            coord_set.add((r, c))
        
        # 위험 상황인 좌표 개수 update
        answer += len(danger_coord_set)
    
    return answer