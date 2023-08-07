def solution(answers):
    answer = []
    stu_1 = [1, 2, 3, 4, 5]
    stu_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    stu_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0, 0, 0]
    
    for i in range(len(answers)):
        if answers[i] == stu_1[i%5]:
            score[0] += 1
        if answers[i] == stu_2[i%8]:
            score[1] += 1
        if answers[i] == stu_3[i%10]:
            score[2] += 1
            
    for idx, count in enumerate(score):
        if count == max(score):
            answer.append(idx + 1)
        
    return answer