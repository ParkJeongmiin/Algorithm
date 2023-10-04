def solution(numbers):
    answer = [-1] * len(numbers)
    stack = []
    
    for idx in range(len(numbers)):
        while stack and numbers[stack[-1]] < numbers[idx]:
            answer[stack.pop()] = numbers[idx]
        stack.append(idx)
        
    return answer