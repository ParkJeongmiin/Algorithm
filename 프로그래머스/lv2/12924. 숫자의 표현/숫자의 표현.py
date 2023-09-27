def solution(n):
    answer = 0
    
    for start in range(1, n+1):
        total = 0
        num = start
        
        while total <= n:
            total += num
            num += 1
            
            if total == n:
                answer += 1
    
    return answer