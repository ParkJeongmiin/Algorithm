def solution(prices):
    stack = []
    answer = [0] * len(prices)
    
    # 스택 풀이
    for idx, price in enumerate(prices):
        while stack and prices[stack[-1]] > price:  # 하락세인 경우
            past_idx = stack.pop()                  # pop
            answer[past_idx] = idx - past_idx       # 시간 초기화
        stack.append(idx)
        
    for idx in stack:
        answer[idx] = len(prices) - idx - 1
            
    return answer