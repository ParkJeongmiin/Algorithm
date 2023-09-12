import heapq

def solution(jobs):
    answer, time, count = 0, 0, 0   # 정답, 현재시간, 완료한 작업 갯수
    start = -1
    heap = []
    
    # 모든 작업이 완료되면 종료
    while count < len(jobs):
        """ heap에 요청 가능한 작업 추가 """
        for job in jobs:
            if start < job[0] <= time:  # 작업 도중에 들어온 요청이 있으면 heap에 추가
                heapq.heappush(heap, [job[1], job[0]])
                
        if len(heap) > 0:
            cur_pro = heapq.heappop(heap)   # 작업 시간
            start = time                    # 작업 시작 시간
            time += cur_pro[0]              # 현재시간
            answer += time - cur_pro[1]     # 현재시간 - 요청 시간 = 요청 to 작업완료 시간
            count += 1
        else:
            time += 1

    return answer // len(jobs)