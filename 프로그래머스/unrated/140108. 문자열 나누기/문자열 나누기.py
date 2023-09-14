"""
1. s에서 한 글자씩 가져온다.
2. word에 하나씩 넣는다.
3. dict[char] += 1로 각각의 나온 횟수를 센다.
4. word의 첫번째 원소의 value 랑 dict의 value들의 합 - 첫번째 원소의 value가 같아지면
    1) result += 1
    2) word, dict 초기화
5. 다 돌았는데 word에 원소가 남아있다면 result += 1하고 종료.
"""

def solution(s):
    answer = 0
    word = []
    dict = {}
    
    for char in s:
        word.append(char)
        if char not in dict:
            dict[char] = 1
        else:
            dict[char] += 1
        
        if dict[word[0]] == (sum(dict.values()) - dict[word[0]]):
            answer += 1
            word = []
            dict = {}
            
    if len(word) > 0:
        answer += 1
    
    return answer