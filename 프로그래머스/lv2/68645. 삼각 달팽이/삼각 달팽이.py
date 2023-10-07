def solution(n):
    answer = []
    
    maps = [[0 for col in range(1, row + 1)] for row in range(1, n + 1)]     # 빈 삼각형 만들기
    
    y, x = -1, 0        # 제일 위에칸을 먼저 채워줘야해서 그 위의 칸에서 출발
    value = 1
    
    for dir in range(n):
        for _ in range(dir, n):
            if dir % 3 == 0:
                y += 1
            elif dir % 3 == 1:
                x += 1
            else:
                y -= 1
                x -= 1
                
            maps[y][x] = value
            value += 1
    
    for row in maps:
        for num in row:
            answer.append(num)
    
    return answer