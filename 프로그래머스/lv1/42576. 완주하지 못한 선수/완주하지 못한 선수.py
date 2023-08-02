def solution(participant, completion):
    
    hash_value = 0
    hash_table = {}
    
    for part_name in participant:
        hash_table[hash(part_name)] = part_name # {이름별 해시값 : 선수 이름}인 Hash table 생성
        hash_value += int(hash(part_name))
        
    for comp_name in completion:
        hash_value -= int(hash(comp_name))
        
    answer = hash_table[hash_value]
    return answer