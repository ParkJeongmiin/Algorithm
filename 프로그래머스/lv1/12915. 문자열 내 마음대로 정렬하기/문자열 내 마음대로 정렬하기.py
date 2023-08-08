def solution(strings, n):
    
    # 먼저 단어를 사전식으로 정렬
    # n번째 글자를 기준으로 정렬
    answer = sorted(strings, key = lambda x: (x[n], x))
    
    return answer