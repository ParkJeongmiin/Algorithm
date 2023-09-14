"""
1. dict : {음식 번호 : 한 선수가 먹는 개수}
    dict[idx] = food[idx] // 2
2. (for) idx in range(1, len(dict) + 1)
    1) answer.append(str(idx) * dict[idx])
3. answer.append('0')
4. answer.append()
"""

def solution(food):
    answer = ''
    dict = {}
    player_list = ''
    
    for idx in range(1, len(food)):
        if food[idx] // 2:
            dict[idx] = food[idx] // 2
    
    for idx in dict:
        player_list += str(idx) * dict[idx]
        
    answer = player_list + '0' + player_list[::-1]
            
    
    return answer