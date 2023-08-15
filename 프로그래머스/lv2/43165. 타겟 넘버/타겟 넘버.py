answer = 0

def dfs(idx, numbers, target, value):
    global answer
    
    length = len(numbers)
    
    # 전부 다 계산했을 때, target 값과 같은 경우, 정답 1 증가
    if idx == length and target == value:
        answer += 1
        return
    
    # 전부 다 계산했을 때, target 값과 다른 경우
    if idx == length:
        return
    
    # 현재 값을 +, -해서 value로 설정, 다음 index 값을 계산하기 위해 dfs 반복
    dfs(idx + 1, numbers, target, value + numbers[idx])
    dfs(idx + 1, numbers, target, value - numbers[idx])

def solution(numbers, target):
    global answer
    dfs(0, numbers, target, 0)
    return answer