def solution(n):
    
    if n <= 2:
        return n
    else:
        a, b = 1, 2
    
        for _ in range(n-1):
            a, b = b, a+b
    
    return a % 1000000007