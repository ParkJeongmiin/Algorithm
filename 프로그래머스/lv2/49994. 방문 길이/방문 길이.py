def solution(dirs):
    answer = 0
    
    move_dic = {'U' : (-1, 0), 'D' : (1, 0), 'L' : (0, -1), 'R' : (0, 1)}
    moved = set()
    
    y, x = 5, 5
    
    for dir in dirs:
        ny = y + move_dic[dir][0]
        nx = x + move_dic[dir][1]
        
        if 0 <= ny <= 10 and 0 <= nx <= 10:
            moved.add(((y, x), (ny,nx)))
            moved.add(((ny, nx), (y, x)))
            
            y, x = ny, nx
    
    return len(moved) // 2
'''
dirs = 명령

return 처음 걸어본 길이

방문결과를 받아서 False(= 처음 걸어보는 길 = answer += 1), Treu(=전에 걸었던 길 = 다음 명령 수행)
'''