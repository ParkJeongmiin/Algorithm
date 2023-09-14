"""
t 에서 p 길이만큼 잘라서 t[idx : idx + len(p)] <= p: answer += 1
"""

def solution(t, p):
    answer = 0
    
    for idx in range(len(t) - len(p) + 1):
        if t[idx: idx + len(p)] <= p:
            answer += 1
    
    return answer