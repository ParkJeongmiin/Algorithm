import sys


def solution(cost, hint):
    INF = sys.maxsize
    answer = INF
    n = len(cost)
    
    # 가능한 모든 구매 시나리오 구성(bit masking)
    # 모든 시나리오 순회
    for mask in range(2 ** n):
        hint_counts = [0] * n    # stage 별 힌트권 개수(0-based idx)
        bundle_cost = 0
        
        for stage_idx in range(n - 1):  # 단계별 번들 구매 시나리오 진행
            if mask & (1 << stage_idx):
                
                for i in range(len(hint[stage_idx])):
                    if i == 0:
                        bundle_cost += hint[stage_idx][i]
                    else:
                        hint_counts[hint[stage_idx][i] - 1] += 1 
        
        # 문제 별 해결 비용 계산
        # 힌트권 사용 가능 횟수 초과한 경우 예외 처리
        complete_cost = 0
        for i, count in enumerate(hint_counts):
            if count < n:
                complete_cost += cost[i][count]
            else:
                complete_cost += cost[i][-1]
                                         
        answer = min(answer, complete_cost + bundle_cost)
    
    return answer

