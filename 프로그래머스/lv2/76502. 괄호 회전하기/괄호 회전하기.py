'''
스택 + 큐

1. deque rotate(-1)
2. popleft()해서 스택에 하나씩 넣는다.
3. 스택의 마지막 2개가 [], (), {} 중에 하나면 pop()해서 빼내기
4. len(stack) == 0 : count += 1
'''
from collections import deque
import copy

def solution(s):
    answer = 0
    s = deque(list(s))
    
    for i in range(len(s)):
        s.rotate(-1)
        
        input_s = copy.deepcopy(s)
        stack = []
        
        for _ in range(len(input_s)):
            stack.append(input_s.popleft())
            
            if stack[-2:] == ['(', ')'] or stack[-2:] == ['[', ']'] or stack[-2:] == ['{', '}']:
                stack.pop()
                stack.pop()
            
        if len(stack) == 0:
            answer += 1
    
    return answer