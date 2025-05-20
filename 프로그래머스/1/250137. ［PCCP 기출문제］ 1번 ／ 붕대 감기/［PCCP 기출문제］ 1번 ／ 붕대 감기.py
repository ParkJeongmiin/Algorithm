def solution(bandage, health, attacks):
    # 확인해야 하는 변수 초기화
    cur_health = health
    cur_time = 0
    
    # 공격 정보를 순회하면서 체력 정보 update
    for attack_time, damage in attacks:
        # 회복 가능한 시간을 계산하고 update
        bandage_time = 0 if (attack_time - cur_time) == 1 else (attack_time - cur_time - 1)
        
        # 회복 시간에 따른 회복량 계산
        if bandage_time // bandage[0]:
            cur_health += bandage[1] * bandage_time + bandage[2] * (bandage_time // bandage[0])
        else:
            cur_health += bandage[1] * bandage_time
            
        # 현재 채력의 최대, 최소 조건이 충족하는지 체크
        if cur_health > health:
            cur_health = health
        
        # 수정된 체력을 바탕으로 데미지 계산
        cur_health -= damage
        
        if cur_health <= 0:
            return -1
        
        # 시간을 현재 시간으로 초기화
        cur_time = attack_time

    return cur_health