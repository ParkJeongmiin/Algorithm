def solution(storey):
    answer = 0
    
    while storey != 0:
        
        # 숫자 제일 뒤에 한자리 가져오기
        check_num = storey % 10
        storey = storey // 10
        
        if check_num < 5:       # 5 미만이면 -1 로 전부 쓴다.
            answer += check_num
        elif check_num == 5:
            answer += 5
            
            if storey % 10 >= 5:
                storey += 1
        elif check_num > 5:
            answer += 10 - check_num
            storey += 1
    
    return answer