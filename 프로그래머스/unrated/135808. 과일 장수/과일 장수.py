"""
한 상자 m 개
가장 낮은 점수 p -> p * m

최대 이익
- 점수가 제일 높은 사과들 먼저 채운다.
sort(reverse = True) : 내림차순

1. 버리는 사과의 개수를 구한다. : len(score) % m = waste_apple
2. 오름차순으로 정리하고 score[waste_apple:]
3. score를 m개 씩 나눠서 2차원 배열에 넣는다.
4. 각 행별로 최소값을 구한다.
5. answer += 최소값 * m
"""

def solution(k, m, score):
    answer = 0
    
    # 버리는 사과는 미리 버린다.
    waste_apple = len(score) % m
    score.sort()
    score = score[waste_apple:]
    
    # 앞에서부터 m 개 씩 나눠서 2차원 배열에 담는다.
    box = []
    for idx in range(0, len(score), m):
        # box.append(min(score[idx: idx + m]))
        answer += score[idx] * m
    
    return answer