def solution(n, m, section):
    """
    section[0]으로 룰러 이동.
    다음 원소가 roller 범위 내 : 통과
                     범위 밖 : answer + 1하고 다음 원소로 이동
    """
    answer = 1
    start = section[0]
    
    for section in section:
        if section - start >= m:
            start = section
            answer += 1
    
    return answer