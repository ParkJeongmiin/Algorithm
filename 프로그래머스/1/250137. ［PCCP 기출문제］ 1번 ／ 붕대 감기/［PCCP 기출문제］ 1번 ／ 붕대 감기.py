def solution(bandage, health, attacks):
    # 확인해야 하는 변수 초기화
    cur_health = health
    cur_time = 1
    
    # 공격 정보를 순회하면서 체력 정보 update
    for attack_time, damage in attacks:
        heal_time = attack_time - cur_time
        cur_health += heal_time * bandage[1] + (heal_time // bandage[0]) * bandage[2]
        
        # 현재 채력의 최대, 최소 조건이 충족하는지 체크
        if cur_health > health:
            cur_health = health
        
        # 수정된 체력을 바탕으로 데미지 계산
        cur_health -= damage
        
        if cur_health <= 0:
            return -1
        
        # 시간을 현재 시간으로 초기화
        cur_time = attack_time + 1

    return cur_health