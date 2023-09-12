import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)
    
    while scoville[0] < K:                              # min이 K 이상이면 종료
        min_val = heapq.heappop(scoville)               # 제일 작은 값 pop
        next_val = heapq.heappop(scoville)              # 그 다음 작은 값 pop
        new_val = min_val + next_val * 2                # 계산
        heapq.heappush(scoville, new_val)               # 계산한 값 push
        answer += 1                                     # 횟수 증가
        
        if len(scoville) == 1 and scoville[0] < K:
            return -1
    
    return answer