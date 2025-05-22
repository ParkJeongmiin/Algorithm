def solution(h1, m1, s1, h2, m2, s2):
    answer = 0
    
    start = h1 * 3600 + m1 * 60 + s1
    end = h2 * 3600 + m2 * 60 + s2
    
    # 1초씩 더해가며 계산할 때, 정오, 정각은 포함되지 않기 때문에 예외 처리
    if start == 0 * 3600 or start == 12 * 3600:
        answer += 1
        
    while start < end:
        # 현재 각도 계산
        hDegree = (start / 120) % 360
        mDegree = (start / 10) % 360
        sDegree = (start * 6) % 360
        
        # 1초 지난 뒤, 각도 계산
        hNextDegree = 360 if (start + 1) / 120 % 360 == 0 else (start + 1) / 120 % 360
        mNextDegree = 360 if (start + 1) / 10 % 360 == 0 else (start + 1) /10 % 360
        sNextDegree = 360 if (start + 1) * 6 % 360 == 0 else (start + 1) * 6 % 360
        
        # 초침이 지나갔는지 체크
        # 시침, 초침
        if sDegree < hDegree and sNextDegree >= hNextDegree:
            answer += 1
        # 분침, 초침
        if sDegree < mDegree and sNextDegree >= mNextDegree:
            answer += 1
            
        # 시침, 분침, 초침 동시에 겹치는 경우 예외 처리
        if sNextDegree == hNextDegree and hNextDegree == mNextDegree:
            answer -= 1
        
        start += 1
        
    return answer