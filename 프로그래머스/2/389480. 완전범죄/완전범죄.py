def solution(info, n, m):    
    dp = [[n for _ in range(m)] for _ in range(len(info) + 1)]  # dp table 초기화
    dp[0][0] = 0        # dp[i][j] = i 번째 물건에서 B의 흔적이 j인 경우, A의 흔적 합
    
    for i in range(1, len(info) + 1):
        cur_a, cur_b = info[i - 1][0], info[i - 1][1]   # 현재 확인하는 물건의 흔적
        
        for j in range(m):
            dp[i][j] = min(dp[i][j], dp[i - 1][j] + cur_a)      # A가 훔친 경우
            
            if j + cur_b < m:   # B가 훔친 경우
                """
                i번 째 물건에서 B를 선택했을 때, 범위를 초과하지 않는 모든 경우의 수 체크
                A의 값에는 영향을 주지 않기 때문에 이전 값을 그대로 가져옵니다.
                """
                dp[i][j + cur_b] = min(dp[i][j + cur_b], dp[i - 1][j])
    
    # 출력값 결정
    answer = n
    for j in range(m):
        answer = min(answer, dp[-1][j])
    
    return answer if answer < n else -1