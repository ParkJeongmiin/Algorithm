'''
모든 종류의 보석을 1개 이상 포함하는 가장 짧은 구간을 찾아서 구매
== 특정 구간 내에서 특정 원소의 개수를 구하는 문제 ==> 투 포인터

gems = 진열된 보석

return = 조건을 만족하는 가장 짧은 구간의 [시작 번호, 끝 번호]
         구간이 여러 개이면 '시작 번호가 가장 작은 구간'
         
투포인터
보석의 종류 = set(gems)

dic에 보석의 종류가 다 없을 때
    1. end += 1
    2. dic에 새로운 보석 추가
보석이 다 있으면
    1. (새로 구한 진열대 수)가 (기존의 진열대 수)보다 작으면 answer를 갱신
    2. 시작점의 보석을 빼주기
    3. 시작점 갱신
'''

def solution(gems):
    
    # 보석의 종류, 진열대 길이
    kind = len(set(gems))
    size = len(gems)
    answer = [0, size - 1]
    
    # dic 초기화 {종류 : 개수}
    dic = {gems[0] : 1}
    start, end = 0, 0
    
    # 끝까지 비교해보고 종료
    while end < size:
        
        if len(dic) < kind:
            end += 1
            if end == size: break
            dic[gems[end]] = dic.get(gems[end], 0) + 1
        else:
            if (end - start + 1) < (answer[1] - answer[0] + 1): answer = [start, end]
        
            if dic[gems[start]] == 1:
                del dic[gems[start]]
            else:
                dic[gems[start]] -= 1
                
            start += 1
            
    answer[0] += 1
    answer[1] += 1
    
    return answer