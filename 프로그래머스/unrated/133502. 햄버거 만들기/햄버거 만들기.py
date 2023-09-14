"""
1개 햄버거 = [1, 2, 3, 1]

스택(LIFO)

while ingredient:
1. ingredient에서 하나씩 popleft() 해서 now_element.append()
2. len(now_element) >= 4:
    1) 뒤에서 부터 4개가 [1,2,3,1] 이면 : pop 4번, answer += 1
            
"""
from collections import deque

def solution(ingredient):
    answer = 0
    ingredient = deque(ingredient)
    now_element = []
    
    while ingredient:
        now_element.append(ingredient.popleft())
        
        if len(now_element) >= 4:
            if now_element[-4:] == [1, 2, 3, 1]:
                answer += 1
                now_element.pop()
                now_element.pop()
                now_element.pop()
                now_element.pop()
                
    
    return answer