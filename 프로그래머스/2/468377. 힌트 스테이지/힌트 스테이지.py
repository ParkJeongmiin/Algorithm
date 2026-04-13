import sys


def solution(cost, hint):
    answer = sys.maxsize
    n = len(cost)
    
    # 힌트 번들은 n-1개만 있기 때문에, 가능한 구매 시나리오는 2 ^ (n - 1)
    total_scenarios = 1 << (n - 1)
    
    # 가능한 모든 구매 시나리오 구성(bit masking)
    # 모든 시나리오 순회
    for mask in range(total_scenarios):
        hint_counts = [0] * n    # stage 별 힌트권 개수(0-based idx)
        bundle_cost = 0
        
        for stage_idx in range(n - 1):  # 단계별 번들 구매 시나리오 진행
            if mask & (1 << stage_idx):
                
                # 리스트 언팩킹으로 가독성 강화
                price, *tickets = hint[stage_idx]
                bundle_cost += price
                
                for ticket in tickets:
                    hint_counts[ticket - 1] += 1 
        
        # 문제 별 해결 비용 계산
        # 힌트권 사용 가능 횟수 초과한 경우 예외 처리
        complete_cost = 0
        for i, count in enumerate(hint_counts):
            complete_cost += cost[i][min(count, n - 1)]
            
        answer = min(answer, complete_cost + bundle_cost)
    
    return answer
