"""
개인 정보 n 개
모든 달은 28일 있다고 가정

today : 오늘 날짜
terms : "약관종류(영어 대문자)  유효기간(달 수)" 1차원 배열
privacies : "날짜(YYYY.MM.DD)   약관종류" 1차원 배열 "1번부터 시작"

*** YYYY.MM.DD를 모두 day 단위로 변환해서 비교 ***
YYYY * 12 * 28 + MM * 28 + DD

1. terms -> split()해서 몇 달 더해야하는지 {종류 : int(month) * 28} 생성  - OK
2. privacies split() -> [날짜, 종류] 2차원 배열로 변경 - OK
3. for i in range(len(privacies))
    1) 종류 불러와서 terms에서 value 값 불러오기
    2) 날짜 불러와서 value 값 더해주기
    3) if 오늘 날짜 < 더한 날짜:    answer.append(i+1)
"""

def solution(today, terms, privacies):
    answer = []
    dict = {}
    new_privacies = []
    
    # 오늘 날짜 day 단위로 변환
    year, month, day = map(int, today.split('.'))
    today = year * 12 * 28 + month * 28 + day
    
    # {종류 : 유효기간(day)} 생성
    for term in terms:
        dict[term.split()[0]] = int(term.split()[1]) * 28
        
    # [[시작날짜, 종류]] 생성
    for pri in privacies:
        start_date, kind = pri.split()
        year, month, day = map(int, start_date.split('.'))
        start_date = year * 12 * 28 + month * 28 + day
        new_privacies.append([start_date, kind])
        
    for idx in range(len(new_privacies)):  
        if dict[new_privacies[idx][1]] + new_privacies[idx][0] <= today: # 저장 만료 날짜 < 오늘 날짜
            answer.append(idx + 1)
    
    return answer