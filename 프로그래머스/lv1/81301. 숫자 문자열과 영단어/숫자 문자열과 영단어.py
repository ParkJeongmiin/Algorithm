'''
    return <= 20억 이하
    
    s = one4seveneight ==> 1478
    
    word_list ['zero', 'one', ...]
    dict = {단어 : '숫자'}
    
    if word in word_lsit:
        s.replace(word, dict[word])
'''

def solution(s):
    answer = 0
    
    word_list = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    dict = {word_list[i] : str(i) for i in range(len(word_list))}
    
    for word in word_list:
        if word in s:
            s = s.replace(word, dict[word])
    
    answer = int(s)
    
    return answer