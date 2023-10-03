def solution(people, limit):
    answer = 0
    
    people.sort()
    
    # 투 포인터를 이용해 짝 지을 수 있는 사람 수 확인
    front = 0
    back = len(people) - 1
    
    while front < back:     # 서로를 넘어가게 되면 종료
        if people[front] + people[back] <= limit:       # 2명이서 탈 수 있는 경우가 몇 개인지 계산
            front += 1
            answer += 1
        back -= 1
    
    return len(people) - answer