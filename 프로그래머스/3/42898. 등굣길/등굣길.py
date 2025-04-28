def solution(m, n, puddles):    
    # table 선언
    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
    dp[1][1] = 1    # 시작 위치(집) 값 설정
    
    # 웅덩이 구간 미리 확인
    for i, j in puddles:
        dp[j][i] = -1
    
    # 경우의 수 계산
    for i in range(1, n + 1):
        for j in range(1, m + 1):            
            if dp[i][j] == -1:
                dp[i][j] = 0
            else:
                dp[i][j] += (dp[i - 1][j] + dp[i][j - 1]) % 1000000007
        
    return dp[n][m] % 1000000007
