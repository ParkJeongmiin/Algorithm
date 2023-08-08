def solution(brown, yellow):
    answer = []
    width = []
    height = []
    
    for i in range(1, yellow + 1):
        if yellow % i == 0 and i >= (yellow // i):  # (yellow의 약수이고) and (a > b) 이면 배열에 추가
            width.append(i)
            height.append(yellow//i)
    
    for i in range(len(width)):
        if ((width[i] + 2) * 2 + height[i] * 2) == brown:
            answer.append(width[i]+2)
            answer.append(height[i]+2)
    
    return answer