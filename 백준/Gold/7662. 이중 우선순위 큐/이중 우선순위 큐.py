import sys
import heapq

# ----- input -----
input = sys.stdin.readline
T = int(input())

# ----- code -----
for t in range(T):
    k = int(input())

    max_heap = []
    min_heap = []
    visited = [False] * k  # 각 노드의 유효성 검사용

    for i in range(k):
        c, v = input().split()
        v = int(v)

        if c == "I":
            heapq.heappush(max_heap, (-v, i))
            heapq.heappush(min_heap, (v, i))
            visited[i] = True  # 해당 노드 활성화

        elif c == "D":
            if v == 1:  # 최댓값 삭제
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)

                if max_heap:
                    visited[max_heap[0][1]] = False
                    heapq.heappop(max_heap)
            else:  # 최솟값 삭제
                while min_heap and not visited[min_heap[0][1]]:
                    heapq.heappop(min_heap)

                if min_heap:
                    visited[min_heap[0][1]] = False
                    heapq.heappop(min_heap)

    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)

    if not min_heap or not max_heap:
        print("EMPTY")
    else:
        print(f"{-max_heap[0][0]} {min_heap[0][0]}")
