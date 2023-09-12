import heapq
from collections import deque

def solution(operations):
    answer = [] # [max, min]
    operations = deque(operations)
    heap = []
    sort_heap = []
    
    while operations:
        data = operations.popleft()
        word, num = data.split()
        
        if word == "I":
            heapq.heappush(heap, int(num))
            
        if heap and word == "D":
            if num == "1":
                heap.remove(max(heap))
            elif num == "-1":
                heapq.heappop(heap)
    
    while heap:
        sort_heap.append(heapq.heappop(heap))
    
    if len(sort_heap) > 0:
        answer.append(sort_heap[-1])
        answer.append(sort_heap[0])
    else:
        answer = [0, 0]
    
    return answer