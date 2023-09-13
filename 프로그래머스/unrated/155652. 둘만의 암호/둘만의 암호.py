"""
1. s에서 한 글자씩 불러온다.
2. ASCII 코드 스킵만큼 한 개씩 늘린다.    a(97)~z(122)  A(65)~Z(90)
3. ascii not in skip: count += 1
4. result.append(new_char)
5. answer += chr(ascii)
"""
    

def solution(s, skip, index):
    answer = ''
    
    for char in s:          # 한 글자씩 가져온다.
        ascii = ord(char)   # ASCII 코드로 변환
        count = 0
        
        while count != index:   # skip은 포함하지 않고 카운트한 횟수가 index와 같아지면 종료
            ascii += 1      # skip만큼 하나씩 글자 변환
            
            if ascii == 123:    # z에서 1 더해지면 a로 변환
                ascii = 97
                
            if chr(ascii) not in skip:   # skip에 없어야 카운트
                count += 1
        
        answer += chr(ascii)
    return answer