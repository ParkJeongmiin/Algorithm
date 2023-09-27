def solution(s):
    answer = []
    
    s = s.split(' ')
    
    for word in s:
        if word:
            answer.append(word[0].upper() + word[1:].lower())
        else:   # 연속된 공백문자 케이스 해결
            answer.append(word)
    
    return ' '.join(answer)