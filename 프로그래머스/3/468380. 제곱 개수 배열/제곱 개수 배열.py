def solution(arr, l, r):
    N = len(arr)
    total_len = sum(arr)
    
    l -= 1
    r -= 1
    W = r - l + 1
    
    # 인덱스(l, r)을 통해 (그룹 번호, 그룹 내 위치)를 반환하는 함수
    def get_pos(target_idx):
        curr_len = 0
        for i in range(N):
            if curr_len + arr[i] > target_idx:
                return i, target_idx - curr_len
            curr_len += arr[i]
        return N - 1, 0
    
    # K 계산
    l_group, l_offset = get_pos(l)
    r_group, r_offset = get_pos(r)
    
    K = 0
    if l_group == r_group:
        K = arr[l_group] * W
    else:
        K += arr[l_group] * (arr[l_group] - l_offset)
        for i in range(l_group + 1, r_group):
            K += arr[i] ** 2
        K += arr[r_group] * (r_offset + 1)
    
    # 초기 윈도우 세팅
    start_r_group, start_r_offset = get_pos(W - 1)
    S = 0
    if start_r_group == 0:
        S = arr[0] * W
    else:
        S += arr[0] ** 2
        for i in range(1, start_r_group):
            S += arr[i] ** 2
        S += arr[start_r_group] * (start_r_offset + 1)
    
    # C, 단방향 탐색
    C = 0
    if S == K:
        C += 1
        
    if W < total_len:
        curr_l_group = 0        # out 원소의 그룹
        curr_l_rem = arr[0]     # 남은 out 원소 개수
        
        curr_r_group, curr_r_offset = get_pos(W)
        curr_r_rem = arr[curr_r_group] - curr_r_offset
        
        while curr_r_group < N:
            in_val = arr[curr_r_group]
            out_val = arr[curr_l_group]
            
            # 두 포인터 중 먼저 그룹 경계에 도달하기 까지 최대 이동 거리
            jump = min(curr_l_rem, curr_r_rem)
            diff = in_val - out_val
            
            if diff == 0:
                if S == K:
                    C += jump
            else:
                # 합이 선형적으로 변하는 구간
                K_diff = K - S
                if K_diff % diff == 0:  # 정수 이동만으로 K에 도달할 수 있는지 판단
                    step = K_diff // diff
                    if 1 <= step <= jump:
                        C += 1
                        
            # jump 이동만큼 window 합, 잔여 원소 개수 갱신
            S += jump * diff
            curr_l_rem -= jump
            curr_r_rem -= jump
            
            # 왼쪽 포인터가 그룹을 벗어나면 다음 그룹으로 이동
            if curr_l_rem == 0:
                curr_l_group += 1
                if curr_l_group < N:
                    curr_l_rem = arr[curr_l_group]
                    
            # 오른쪽 포인터가 그룹을 벗어나면 다음 그룹으로 이동
            if curr_r_rem == 0:
                curr_r_group += 1
                if curr_r_group < N:
                    curr_r_rem = arr[curr_r_group]
    
    return [K, C]