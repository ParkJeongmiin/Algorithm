def solution(picks, minerals):
    answer = 0
    
    # 캘 수 있는 광물 개수
    can_mine = min(picks[0] * 5 + picks[1] * 5 + picks[2] * 5, len(minerals))
    
    if can_mine < len(minerals):
        minerals = minerals[:can_mine]
        
    # 광물별 개수 구하기
    count_list = [[0, 0, 0] for _ in range(len(minerals) // 5 + 1)]
    for idx in range(len(minerals)):
        if minerals[idx] == 'diamond':
            count_list[idx // 5][0] += 1
        elif minerals[idx] == 'iron':
            count_list[idx // 5][1] += 1
        elif minerals[idx] == 'stone':
            count_list[idx // 5][2] += 1
            
    sorted_count_list = sorted(count_list, key = lambda x : (-x[0], -x[1], -x[2]))
    
    # 피로도 계산
    for group in sorted_count_list:
        dia, iron, stone = group
        
        for idx in range(len(picks)):
            if idx == 0 and picks[idx] > 0:
                picks[idx] -= 1
                answer += dia + iron + stone
                break
            elif idx == 1 and picks[idx] > 0:
                picks[idx] -= 1
                answer += 5 * dia + iron + stone
                break
            elif idx == 2 and picks[idx] > 0:
                picks[idx] -= 1
                answer += 25 * dia + 5 * iron + stone
                break
    
    return answer