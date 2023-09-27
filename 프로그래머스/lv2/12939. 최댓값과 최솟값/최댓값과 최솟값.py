def solution(s):
    answer = ''
    
    s = list(map(int, s.split()))
    s.sort()
    
    min = str(s[0])
    max = str(s[-1])
    answer = min + ' ' + max
    
    return answer