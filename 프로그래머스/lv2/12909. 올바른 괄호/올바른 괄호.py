from collections import deque

def solution(s):
    answer = True
    recv = []
    s = deque(list(s))
    
    while len(s) != 0:
        recv.append(s.popleft())
        
        if recv[-2:] == ["(",")"]:
            recv.pop()
            recv.pop()
    
    if len(recv) == 0:
        answer = True
    else:
        answer = False

    return answer