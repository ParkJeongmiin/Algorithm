def solution(board, moves):
    answer = 0
    stack = []
    
    for move in moves:
        for floor in range(len(board)):
            cur = board[floor][move - 1]
            
            if cur != 0:
                board[floor][move - 1] = 0
                
                if not stack or stack[-1] != cur:
                    stack.append(cur)
                elif stack[-1] == cur:
                    stack.pop()
                    answer += 2
                break
                
    return answer