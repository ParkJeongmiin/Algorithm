"""
조합(Combinations)

1. 가능한 조합들 list로 만들기
2. 각 행 별로 sum()
3. count(0)
"""
from itertools import combinations

def solution(number):
    answer = 0
    comb = []
    sum_list = []
    
    comb = list(combinations(number, 3))
    
    for idx in range(len(comb)):
        sum_list.append(sum(comb[idx]))
        
    answer = sum_list.count(0)
    
    return answer