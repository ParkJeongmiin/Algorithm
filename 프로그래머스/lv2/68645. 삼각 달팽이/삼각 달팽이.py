def make_triangle(y, x, depth, cur_val, maps):
    if depth <= 0:
        return maps
    if depth == 1:
        maps[y][x] = cur_val
    
    for row in range(depth):
        maps[y + row][x] = cur_val
        cur_val += 1
    for col in range(1, depth):
        maps[y + depth -1][x + col] = cur_val
        cur_val += 1
    for idx in range(1, depth-1):
        maps[y + depth - 1 - idx][x + depth - 1 - idx] = cur_val
        cur_val += 1
        
    make_triangle(y + 2, x + 1, depth - 3, cur_val, maps)

def solution(n):
    answer = [[0] * n for n in range(1, n+1)]
    a = []
    
    make_triangle(0, 0, n, 1, answer)
    
    for row in answer:
        for num in row:
            a.append(num)
    
    return a