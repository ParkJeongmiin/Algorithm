from itertools import combinations


def binary_search(target, case):
    '''특정 값 미만의 눈 갯수를 탐색하는 이진탐색 함수'''
    low = 0
    high = len(case) - 1
    
    while low <= high:
        mid = (low + high) // 2
        
        if case[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
            
    return low
    
    

def simulation_score(case, dice, out, idx, now):
    if idx == len(case):
        out.append(now)
        return
    
    for val in dice[case[idx]]:
        simulation_score(case, dice, out, idx + 1, now + val)


def solution(dice):
    answer = []
    
    # 가능한 주사위 조합 계산
    dice_idx = list(range(len(dice)))
    dice_combinations = list(combinations(dice_idx, len(dice) // 2))
    
    # 주사위 조합 별 합 경우의 수 계산
    scores = {}
    for idx, case in enumerate(dice_combinations): 
        out = []
        simulation_score(case, dice, out, idx=0, now=0)
        out.sort()      # 이분 탐색을 위한 정렬
        scores[idx] = out
        
    # 조합 중에서 가장 많이 이기는 경우 검색
    best_sum = 0
    for key, val in scores.items():
        now_case = val      # 현재 케이스
        other_case = scores[len(dice_combinations) - key - 1]   # 상대방 케이스
        
        # 현재 케이스를 기준으로 상대방을 이기는 횟수 계산
        temp_sum = 0
        for c in now_case:
            temp_sum += binary_search(c, other_case)
            
        # 최고기록과 비교해 정답 갱신
        if temp_sum > best_sum:
            best_sum = temp_sum
            best_case = dice_combinations[key]
            answer = list(map(lambda x: x + 1, sorted(best_case)))
        
    return answer