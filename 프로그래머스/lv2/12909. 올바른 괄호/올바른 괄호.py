def solution(s):
    answer = True
    recv = []
    
    for i in s:
        recv.append(i)
        
        if recv[-2:] == ["(", ")"]:
            recv.pop()
            recv.pop()
    
    if len(recv) == 0:
        answer = True
    else:
        answer = False

    return answer