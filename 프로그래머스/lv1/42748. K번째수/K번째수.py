def solution(array, commands):
    answer = []
    
    """
    commands에서 ijk 받아오기
    array[i+1, j+1] slicing
    sort 해서 [k+1] 번째 숫자 answer.append()
    """
    
    for command in commands:
        i = command[0] - 1
        j = command[1]
        k = command[2] - 1
        
        sorted_array = array[i : j]
        sorted_array.sort()
        answer.append(sorted_array[k])
        
    return answer