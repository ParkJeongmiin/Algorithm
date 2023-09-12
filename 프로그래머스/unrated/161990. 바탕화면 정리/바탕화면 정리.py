def solution(wallpaper):
    answer = []
    col_idx = []
    row_idx = []
    
    # 시작칸 구하기
    # 행으로 확인 -> #이 나오는 행을 모은다. -> (행 모음 중 min) = lux
    #           -> (행 모음 중 max) + 1 = rdx
    # 열로 확인 -> 행 별로 #이 나오는 idx 확인 -> (idx의 모음 중 min) = luy
    #                                       -> (idx의 모음 중 max) + 1 = rdy
    
    # 행으로 확인
    for x in range(len(wallpaper)):
        if '#' in wallpaper[x]:
            col_idx.append(x)
        # 열로 확인
        for y in range(len(wallpaper[x])):
            if wallpaper[x][y] == '#':
                row_idx.append(y)

    # S(lux, luy), E(rdx, rdy) 정의
    lux, rdx = min(col_idx), max(col_idx) + 1
    luy, rdy = min(row_idx), max(row_idx) + 1
    
    return [lux, luy, rdx, rdy]