from collections import deque

def solution(numbers, target):
    
    answer = 0
    queue = deque()     # queue 생성
    
    length = len(numbers)   # 끝났을 때 값 비교를 위해서
    queue.append([-numbers[0], 0])  # 해당 노드의 값, 현재 깊이-1 저장
    queue.append([+numbers[0], 0])
    
    while queue:
        num, i = queue.popleft()
        if i + 1 == length:     # 현재 노드가 마지막 노드이고
            if num == target: answer += 1   # target 과 일치하다면 answer 1 증가
        else:                   # 마지막이 아니라면
            queue.append([num - numbers[i+1], i+1]) # queue에 [node value, 현재 깊이-1] 저장
            queue.append([num + numbers[i+1], i+1])
    
    return answer