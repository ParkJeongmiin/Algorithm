'''
survey[i][0] : 비동의 관련 선택지
survet[i][1] : 동의 관련 선택지

TR RT : 
choice[idx] >= 4: 

dict = {R: 점수, T : 점수, C : 점수, F : 점수, J : 점수 ...}
score = {choice : 점수}
'''

def solution(survey, choices):
    answer = ''
    
    kind = ['R', 'T', 'C', 'F', 'J', 'M', 'A', 'N']
    dict = {_ : 0 for _ in kind}
    
    s = [3, 2, 1, 0, 1, 2, 3]
    score = {i+1 : s[i] for i in range(len(s))}
    
    for sur, choice in zip(survey, choices):
        if choice < 4:
            dict[sur[0]] += score[choice]
        elif choice > 4:
            dict[sur[1]] += score[choice]
            
    # 앞에서 2개씩 쪼개면서 크기 비교해서 answer에 더하기
    for idx in range(0, len(dict), 2):
        if dict[kind[idx]] > dict[kind[idx + 1]]:
            answer += list(dict.keys())[idx]
        elif dict[kind[idx]] < dict[kind[idx + 1]]:
            answer += list(dict.keys())[idx + 1]
        else:
            same_score_kind = list(dict.keys())[idx: idx + 2]
            same_score_kind.sort()
            answer += same_score_kind[0]
    
    return answer