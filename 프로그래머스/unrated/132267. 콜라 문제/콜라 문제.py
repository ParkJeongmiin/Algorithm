"""
빈 병 a개 = 콜라 b병 (단, n < a : 교환 불가)
n = 현재 가지고 있는 빈병

1. 
"""

def solution(a, b, n):
    answer = 0

    while n >= a:
        remain = n % a
        recv = (n//a) * b
    
        n = remain + recv
        # if n >= a:
        #     answer += recv
        # else:
        #     answer += recv
        answer += recv
        
    return answer