def solution(name, yearning, photo):
    answer = []
    hash_table = {}
    sum = 0
    
    for name, yearning in zip(name, yearning):
        hash_table[name] = yearning

    for i in range(len(photo)):
        for photo_name in photo[i]:
            if photo_name in hash_table:
                sum += hash_table[photo_name]
            else:
                sum += 0
                
        answer.append(sum)
        sum = 0
    
    return answer