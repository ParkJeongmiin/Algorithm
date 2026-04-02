def solution(message, spoiler_ranges):
    # 1. 스포일러 구간 매핑
    # 각 인덱스가 스포일러 구간(ID) 정보를 매핑
    msg_len = len(message)
    spoiler_map = [-1] * msg_len
    
    for spoiler_id, (start, end) in enumerate(spoiler_ranges):
        for i in range(start, end + 1):
            spoiler_map[i] = spoiler_id
    
    # 2. 단어 추출
    words_info = []
    curr_word = []
    start_idx = -1
    
    for i, char in enumerate(message):
        if char != " ":
            if start_idx == -1:     # 공백으로 시작하는 경우 처리
                start_idx = i
            curr_word.append(char)
        else:
            if curr_word:
                words_info.append(("".join(curr_word), start_idx, i - 1))
                curr_word = []
                start_idx = -1
    
    if curr_word:       # 마지막 단어 뒤에 공백이 없는 경우 예외처리
        words_info.append(("".join(curr_word), start_idx, msg_len - 1))
    
    # 3. 이미 노출된 단어 필터링, 단어가 최종 공개되는 ID 계산
    blacklisted = set()
    events = [] # (공개 시점 ID, 단어 시작 인덱스, 단어 문자열)
    
    for word_str, start, end in words_info:
        covered_spoilers = set()
        
        # 단어를 구성하는 각 글자가 어떤 스포일러 구간에 포함되는지 확인
        for i in range(start, end + 1):
            if spoiler_map[i] != -1:
                covered_spoilers.add(spoiler_map[i])
                
        # 한 글자도 스포 방지 구간에 속하지 않으면 전부 노출된 단어
        if not covered_spoilers:
            blacklisted.add(word_str)
        else:
            # 단어가 최종적으로 공개되는 스포일러 ID로 저장
            reveal_time = max(covered_spoilers)
            events.append((reveal_time, start, word_str))
    
    # 4. 시뮬레이션 및 중요 단어 집계
    events.sort(key=lambda x: (x[0], x[1])) # 공개 시점(오름차순), 동시 공개 단어(오름차순) 정렬
    
    important_words = set()
    answer = 0
    
    for reveal_time, start, word_str in events:
        if word_str not in blacklisted and word_str not in important_words:
            important_words.add(word_str)
            answer += 1

    return answer