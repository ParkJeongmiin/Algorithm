from collections import Counter

def solution(lottos, win_nums):
    rank = {6:1, 5:2, 4:3, 3:4, 2:5, 1:6, 0:6}
    
    lottos = Counter(lottos)
    win_nums = Counter(win_nums)

    correct_num = len(win_nums) - len(win_nums - lottos)

    good_rank = correct_num + lottos[0]
    bad_rank = correct_num
    
    return [rank[good_rank], rank[bad_rank]]