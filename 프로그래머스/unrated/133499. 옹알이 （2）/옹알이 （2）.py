"""
1. babbling에서 한 단어씩(word) 가져온다.
2. can_speak에서 한 개씩(data) 가져온다.
    1) 같은 단어가 연속으로 나오지 않으면 -> word 중에 발음할 수 있는 말을 공백으로 대체한다.
        (if) data * 2 not in word : word = word.replace(data, '')
3. word가 전부 공백이면 -> 전부 말할 수 있는 단어이므로 answer += 1
    (if) word == '': 
"""
def solution(babbling):
    answer = 0
    can_speak = ['aya', 'ye', 'woo', 'ma']
    
    for babbling in babbling:
        for data in can_speak:
            if data * 2 not in babbling:
                babbling = babbling.replace(data, ' ')
        
        if babbling.isspace():
            answer += 1
    
    return answer