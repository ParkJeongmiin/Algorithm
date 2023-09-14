"""
1. (for) 0 ~ k-1일 까지는 rank.append(score[idx]), score.popleft()
2. while score:
    today_score = score.popleft()
    1) (if) min(명예의 전당) <= today_score
        True : append(today_score) -> sort() -> pop()   오늘 점수 더하고, 정렬해서, 마지막 요소는 빼기
        False : 
    2) answer.append(rank[-1])
"""
def solution(k, score):
    answer = []
    rank = []
    
    for today_score in score:
        
        rank.append(today_score)
    
        if len(rank) > k:
            rank.remove(min(rank))
            
        answer.append(min(rank))
        
    return answer