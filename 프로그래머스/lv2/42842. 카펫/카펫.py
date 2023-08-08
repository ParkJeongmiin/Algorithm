def solution(brown, yellow):
    answer = []
    width = []
    height = []
    
    for i in range(1, int(yellow**(1/2)) + 1):
        if yellow % i == 0:     # yellow의 약수이면 배열에 추가
            width.append(yellow//i)     # 큰 수가 가로에 저장
            height.append(i)
    
    for i in range(len(width)):
        if ((width[i] + 2) * 2 + height[i] * 2) == brown:
            answer.append(width[i]+2)
            answer.append(height[i]+2)
    
    return answer