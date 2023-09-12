def solution(prices):
    size = len(prices)
    answer = [0] * size
    
    for i in range(size):
        for j in range(i+1, size):
            if prices[i] <= prices[j]:   # 상승세이면
                answer[i] += 1
            else:
                answer[i] += 1
                break
                
    return answer