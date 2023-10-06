def solution(lottos, win_nums):
    answer = []
    rank = [6, 6, 5, 4, 3, 2, 1]
    
    correct = 0
    zero_count = 0
    
    for lotto in lottos:
        if lotto in win_nums:
            correct += 1
        elif lotto == 0:
            zero_count += 1
            
    max_count = correct + zero_count
    min_count = correct
    
    return [rank[max_count], rank[min_count]]