def solution(skill, skill_trees):
    answer = 0
    
    for tree in skill_trees:
        stack = ''
        
        for char in tree:
            if char in skill:
                stack += char
                
        for i in range(len(stack)):
            if stack[i] != skill[i]:
                break
        else:
            answer += 1
    
    return answer