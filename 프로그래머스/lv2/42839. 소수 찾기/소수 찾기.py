from itertools import permutations
import math

def check_prime(num):
    if num < 2:         # 1은 제외
        return False
    
    for i in range(2, int(math.sqrt(num)) + 1):
        if num % i == 0:    # 소수 아님
            return False
        
    return True

def solution(numbers):
    num_list = []
    answer = 0
    
    for i in range(1, len(numbers) + 1):
        num_list.append(list(set(map(int, map(''.join, permutations(numbers, i))))))
        # num_list = [ [1자리 조합], [2자리 조합], [3자리 조합], [4자리 조합] ]
        
    new_list = list(set(map(int, sum(num_list, []))))
    
    for number in new_list:
        if check_prime(number) == True:
            answer += 1
    
    return answer