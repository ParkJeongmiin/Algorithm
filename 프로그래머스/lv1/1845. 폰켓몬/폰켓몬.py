def solution(nums):
    
    get_num = len(nums) / 2
    max_num = len(set(nums))
    answer = min(max_num, get_num)
    
    return answer