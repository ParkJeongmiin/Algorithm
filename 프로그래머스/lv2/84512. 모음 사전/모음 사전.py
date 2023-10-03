def find(data, phase, step):  # (사전을 기록할 배열, 현재 문자열, 현재 문자열 길이)
    if step == 6: return      # 최대 5글자 이므로 넘어가면 종료
    if phase != '': data.append(phase)  # 사전에 추가
    
    for char in ['A', 'E', 'I', 'O', 'U']:  # 다음 모음을 불러와 재귀함수 호출
        find(data, ''.join([phase, char]), step + 1)
    
def solution(word):
    answer = 0
    data = []
    find(data, '', 0)
    
    # 만들어진 사전에 주어진 단어가 있는지 검색
    for i in range(len(data)):
        if data[i] == word:
            return i + 1