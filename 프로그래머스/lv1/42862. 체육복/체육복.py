def solution(n, lost, reserve):
    answer = 0
    
    # 차집합 연산
    reserve_set = list(set(reserve) - set(lost))
    lost_set = list(set(lost) - set(reserve))
    
    # 오름차순 정렬
    reserve_set.sort()
    lost_set.sort()
    
    print(reserve_set)
    print(lost_set)
    
    for i in reserve_set :
        if (i-1) in lost_set :
            lost_set.remove(i-1)       
        elif (i+1) in lost_set :
            lost_set.remove(i+1)
    
    answer = n - len(lost_set)
    
    return answer