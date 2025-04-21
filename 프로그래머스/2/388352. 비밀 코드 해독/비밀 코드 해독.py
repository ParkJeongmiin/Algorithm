from itertools import combinations

def solution(n, q, ans):
    answer = 0
    code = list(combinations(range(1, n + 1), 5))  # 전체 가능한 조합
    
    for c in code:
        for i in range(len(q)):
            # 해당 c가 주어진 상황(q, ans)와 동일한지 판단
            if len(set(c) & set(q[i])) != ans[i]:
                break
        else:
            answer += 1
    
    return answer