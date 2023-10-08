def solution(sequence, k):
    answer = []
    
    size = len(sequence)
    front = back = 0
    total = sequence[0]
    
    while back < size:
        length = back - front + 1
        
        if total == k:
            answer.append([length, front, back])
            back += 1
            if back == size: break
            total += sequence[back]
        elif total < k:
            back += 1
            if back == size: break
            total += sequence[back]
        else:
            total -= sequence[front]
            front += 1

    answer = sorted(answer, key = lambda x : (x[0], x[1]))
    
    return [answer[0][1], answer[0][2]]