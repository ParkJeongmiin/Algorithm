def simulation(diffs, times, limit, level):
    """
    퍼즐을 주어진 level로 limit만큼의 제한 시간 안에 풀 수 있는지 검증
    """
    n = len(diffs)
    total_cur = 0   # 퍼즐을 푸는 데 총 걸린 시간
    
    for i in range(n):
        diff = diffs[i]
        time_cur = times[i]
        time_prev = times[i - 1]
        
        if level >= diff:
            total_cur += time_cur
        else:
            total_cur += (time_prev + time_cur) * (diff - level) + time_cur
            
        if total_cur > limit:
            return False
    
    return True


def solution(diffs, times, limit):
    """
    이분 탐색의 최소 / 최대 범위를 산출
    """
    low, high = 1, max(diffs)
    
    while low <= high:
        mid_level = (low + high) // 2   # 현재 범위의 중간값 계산
        
        result = simulation(diffs, times, limit, mid_level)     # 시뮬레이션을 통해 결과를 산출
        
        # 결과가 성공이면, 현재 값보다 상위의 값은 더 이상 안 봐도 됨
        if result:
            high = mid_level - 1
        else:   # 결과가 실패라면, 최소값 보다 작은 값은 더 이상 안 봐도 됨
            low = mid_level + 1
    
    return low