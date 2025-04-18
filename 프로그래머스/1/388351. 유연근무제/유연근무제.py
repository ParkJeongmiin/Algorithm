def solution(schedules, timelogs, startday):
    answer = 0
    
    for i in range(len(schedules)):
        day = startday
        end_time = time2min(schedules[i]) + 10
        
        for j in range(7):
            if day == 6:        # 토요일
                day += 1
                continue
            elif day == 7:      # 일요일
                day = 1
                continue
            else:               # 평일
                if end_time < time2min(timelogs[i][j]):   # 지각
                    break
                else:
                    day += 1
        else:
            answer += 1    
        
    return answer

def time2min(time):
    h = time // 100
    m = time % 100
    return h * 60 + m