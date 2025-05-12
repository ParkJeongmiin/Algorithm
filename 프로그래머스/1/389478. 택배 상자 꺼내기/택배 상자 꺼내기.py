def solution(n, w, num):
    answer = 0
    width = w - 1
    max_row = (n + width) // w
    
    # 꺼내려고 하는 상자의 위치 정보 계산
    y = (num - 1) // w
    x = width - (num - 1) % w if y % 2 else (num - 1) % w
    
    # 위에 있는 상자 번호 계산
    for i in range(y, max_row):
        above_box = i * w + (width - x) if i % 2 else i * w + x
        
        if above_box < n:
            answer += 1        
        
    return answer