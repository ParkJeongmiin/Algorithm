"""
1. s에서 한 개의 글자(find), 자신보다 앞의 있는 글자(check)를 추출
2. find가 check 안에 있는지 확인
    1) True : check를 순서대로 보면서 같은 글자가 있는 i를 location에 추가
              다 돌면, 가장 큰 i가 찾는 글자와 가까운 글자이니까 idx - max(location)해서 answer에 추가
    2) False : answer.append(-1)
"""

def solution(s):
    answer = []
    
    for idx in range(len(s)):
        find = s[idx]
        check = s[:idx]
        location = []
        
        if find in check:       # 앞에 글자 중에 find가 있으면
            for i in range(len(check)):
                if check[i] == find:
                    location.append(i)
            answer.append(idx - max(location))             
        else:
            answer.append(-1)
    
    return answer