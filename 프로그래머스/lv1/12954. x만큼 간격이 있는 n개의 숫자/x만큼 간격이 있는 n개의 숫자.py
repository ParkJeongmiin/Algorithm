def solution(x, n):
    answer = []
    
    for i in range(1, n+1, 1):
        val = x * i
        answer.append(val)

    return answer