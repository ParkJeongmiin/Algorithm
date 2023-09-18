def solution(n, left, right):
    answer = []
    
    for idx in range(left, right + 1):
        answer.append(max(idx // n, idx % n)+1)
        
    return answer