def solution(k, d):
    answer = 0
        
    for x in range(0, d + 1, k):
        answer +=  (((d**2 - x**2) ** (1/2))//k) + 1
    
    return answer
'''
distance => ((x ** 2) + (y ** 2)) ** (1/2)
'''