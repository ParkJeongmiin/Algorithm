n, k = map(int, input().split())
    
coins = []
for _ in range(n):
    coins.append(int(input()))
        
dp = [0] * (k + 1) # DP 테이블 정의
dp[0] = 1          # 초기값 설정

for coin in coins:
    for i in range(coin, k+1):
        # 현재 가지고 있는 코인을 가지고 이전에 계산한 방법들에 추가한 경우의 수 계산
        dp[i] = dp[i] + dp[i - coin]

print(dp[k])