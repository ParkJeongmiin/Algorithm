def solution(keymap, targets):
    answer = []
    
    for target in targets:      # 목표하는 단어 가져오기
        total_count = 0               # 누른 총 횟수
        
        for char in target:     # 목표 단어에서 한 글자씩 가져오기
            flag = False        # 목표 문자열의 작성 가능성 판단
            char_count = 101         # 한개의 문자열 별 횟수
            
            for key in keymap:  # keymap 한 단어씩 가져오기
                if char in key: # key에 char이 포함된다면
                    char_count = min(key.index(char) + 1, char_count) # 이전 값과 비교해서 작은 값으로 저장
                    flag = True # 목표 단어 작성 가능으로 판단
            
            if flag == False:   # key를 끝까지 봤는데 없다면
                total_count = -1
                break
                
            total_count += char_count      # 한 문자에 대한 횟수 업데이트
    
        answer.append(total_count)    # 하나의 단어가 끝나면 총 횟수 answer에 저장하기
    
    return answer