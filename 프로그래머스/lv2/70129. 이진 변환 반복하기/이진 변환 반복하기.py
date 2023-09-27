def solution(s):
    calc_cnt = 0
    delet_cnt = 0
    
    while s != '1':
        # 0 제거하고, 개수 세기
        delet_cnt += s.count('0')
        s = s.replace('0', '')
        
        # 이진변환
        calc_cnt += 1
        s = format(len(s), 'b')
    
    return [calc_cnt, delet_cnt]