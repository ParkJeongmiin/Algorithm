'''
크기별로 분류했을 때 서로 다른 종류의 수를 최소화

* 개수가 많은 순으로 정렬해서, 가장 많은 것 부터 상자에 담는다. * 
1. 크기별 개수 구하기 -> counter
2. 개수가 많은 순으로 정렬하기 -> counter.most_common()
3. 크기, 개수를 가져와서 현재 상자에 있는 개수랑 더해서 이상이 되면 멈추기
'''
from collections import Counter

def solution(k, tangerine):
    cnt = 0
    kind_set = set()
    
    counter = Counter(tangerine)
    sorted_counter = counter.most_common()
    
    for size, num in sorted_counter:
        kind_set.add(size)
        cnt += num
        
        if cnt >= k:
            break
            
    answer = len(kind_set)
    
    return answer