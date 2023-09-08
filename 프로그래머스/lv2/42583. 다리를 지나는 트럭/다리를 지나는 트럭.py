from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    truck_weights = deque(truck_weights)
    bridge = deque([0] * bridge_length) # 다리 위 트럭 위치 현황
    cur_weights = 0                     # 현재 다리 위의 무게 합
    
    while bridge:                       # 다리 위에 어떠한 요소도 없을 때까지 반복
        
        # 모든 동작에 반복되서 따로 뺐음.
        answer += 1
        cur_weights -= bridge[0]
        bridge.popleft()
        
        if truck_weights:
            if cur_weights + truck_weights[0] <= weight:
                cur_weights += truck_weights[0]
                bridge.append(truck_weights.popleft())
            else:
                bridge.append(0)
    
    return answer