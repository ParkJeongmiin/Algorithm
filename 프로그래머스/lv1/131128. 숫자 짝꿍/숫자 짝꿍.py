def solution(X, Y):
    answer = ''
    dict_x = {}
    dict_y = {}
    
    
    for i in range(10):
        i = str(i)
        dict_x[i] = 0
        dict_y[i] = 0
        
    # X, Y에서 각 숫자별 개수 dict에 넣기
    for num in X:
        dict_x[num] += 1
        
    for num in Y:
        dict_y[num] += 1
        
    # list inter section + sort
    for num in range(9, -1, -1):
        num = str(num)
        intersec = min(dict_x[num], dict_y[num])
        
        answer += num * intersec        # 문자열 * 숫자 -> 반복문보다 시간이 적게 걸린다.
        
    if len(answer)  == 0:       # 겹치는 숫자가 아무거도 없다
        return '-1'
    elif len(answer) == answer.count('0'):    # 전체 숫자가 0으로 되어 있으면 길이 == 0의 개수
        return '0'
    else:
        return answer    