import sys
sys.setrecursionlimit(20000)


def solution(depth, money, excavate):
    w = len(depth)
    dp = [[-1] * (w + 2) for _ in range(w + 2)]     # 구간 [L, R]에서 최악의 경우, 최소 굴착 비용 정보
    best_pick = [[0] * (w + 2) for _ in range(w + 2)]   # 구간 [L, R]에서 최우선으로 탐색해야 하는 열 정보
    
    def get_cost(L, R):
        # ----- 1. 기저 조건 -----
        if L > R: return 0                  # 범위 잘못 설정시 비용은 0
        if dp[L][R] != -1: return dp[L][R]  # 이전에 확인한 구간에 대해서는 중복 탐색 방지
    
        if L == R:                          # 한 칸에 대해서만 탐색하면 비용 갱신 후 탐색 종료
            best_pick[L][R] = L
            return depth[L - 1]
        
        # ----- 2. 점화식 계산 (최악의 경우 최소 비용 탐색) -----
        min_cost = float('inf')
        optimal_k = -1
        
        for k in range(L, R + 1):
            curr_cost = depth[k - 1]
            worst_case = max(get_cost(L, k - 1), get_cost(k + 1, R))
            total_cost = curr_cost + worst_case
            
            # 새로운 최소 비용 계산 시, 정보 갱신
            if total_cost < min_cost:
                min_cost = total_cost
                optimal_k = k
                
        # ----- 3. 주어진 구간에 대한 모든 탐색 후 DP 테이블 업데이트 -----
        dp[L][R] = min_cost
        best_pick[L][R] = optimal_k
        return min_cost
        
        
    # ----- 1 단계: 전체 열에 대한 DP 실행 -----
    get_cost(1, w)
    
    # ----- 2 단계: [L, R]을 조절하면서 보물 찾기 시뮬레이션 -----
    left = 1
    right = w
    
    while left <= right:
        k = best_pick[left][right]  # 미리 저장한 최적의 열 조회
        result = excavate(k)        # 보물 위치 정보 확인
        
        if result == 0:
            return k
        elif result == -1:
            right = k - 1
        elif result == 1:
            left = k + 1
    
    return -1
