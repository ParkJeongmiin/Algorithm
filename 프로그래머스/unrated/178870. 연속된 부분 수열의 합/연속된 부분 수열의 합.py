def solution(sequence, k):
    answer = []
    
    size = len(sequence)
    front, back = 0, -1
    total = 0
    
    while front < size:
        if total < k:
            back += 1
            if back == size: break
            total += sequence[back]
        else:
            total -= sequence[front]
            if front >= size:
                break
            front += 1
            
        if total == k:
            answer.append([front, back])
    
    answer = sorted(answer, key = lambda x : (x[1] - x[0], x[0]))
    
    return answer[0]