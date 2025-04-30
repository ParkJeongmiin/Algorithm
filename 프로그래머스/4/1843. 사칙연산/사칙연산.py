def solution(arr):
    INF = int(1e9)
    n = len(arr) // 2 + 1   # 숫자 개수
    
    max_dp = [[-INF for _ in range(n)] for _ in range(n)]       # 최댓값 memo table
    min_dp = [[INF for _ in range(n)] for _ in range(n)]        # 최솟값 memo table
    
    for step in range(n):       # i, j 사이 간격
        for i in range(n-step): # i ~ j까지 연산 수행
            j = i + step
            
            if step == 0:       # 자기 자신까지 최댓값은 자기 자신
                max_dp[i][i] = int(arr[i * 2])
                min_dp[i][i] = int(arr[i * 2])
            else:
                for k in range(i, j):
                    # 최솟값도 계산 중에 필요하기 때문에 tracking 진행
                    if arr[k * 2 + 1] == "+":
                        # + 연산의 경우 크기가 커지는 방향으로 저장
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] + max_dp[k + 1][j])    # max(기존 값, max + max)
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] + min_dp[k + 1][j])    # max(기존 값, min + min)
                    else:
                        # - 연산의 경우 크기가 커지는 방향으로 저장
                        max_dp[i][j] = max(max_dp[i][j], max_dp[i][k] - min_dp[k + 1][j])    # max(기존 값, max - min)
                        min_dp[i][j] = min(min_dp[i][j], min_dp[i][k] - max_dp[k + 1][j])    # min(기존 값, min - max)
    
    return max_dp[0][-1]